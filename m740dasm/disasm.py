from m740dasm.tables import (
    AddressModes,
    Opcodes,
    InstructionLengths,
    )


class Instruction(object):
    __slots__ = ('disasm_template', 'addr_mode', 'opcode', 'operands',
                 'zp_addr', 'immediate', 'abs_addr', 'sp_addr', 'rel_addr',
                 'flow_type')

    def __init__(self, **kwargs):
        self.disasm_template = '' # "lda {abs}"
        self.addr_mode = None     # addressing mode
        self.zp_addr = None       # zero page address
        self.abs_addr = None      # absolute address
        self.sp_addr = None       # special page address
        self.rel_addr = None      # resolved relative address
        self.immediate = None     # immediate value
        self.opcode = None        # opcode byte
        self.operands = ()        # operand bytes
        self.flow_type = None

        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)
            else:
                raise KeyError(k)

    def __len__(self):
        return 1 + len(self.operands)

    def __str__(self):
        disasm = self.disasm_template
        for attr, tpl, fmt in self._disasm_formats:
            v = getattr(self, attr)
            if v is not None:
                disasm = disasm.replace(tpl, fmt % v)
        return disasm

    @property
    def all_bytes(self):
        data = [self.opcode]
        data.extend(self.operands)
        return data

    _disasm_formats = (
        ('opcode',    '{opc}', '0x%02x'),
        ('zp_addr',   '{zp}',  '0x%02x'),
        ('sp_addr',   '{sp}',  '0xff%02x'),
        ('abs_addr',  '{abs}', '0x%04x'),
        ('rel_addr',  '{rel}', '0x%04x'),
        ('immediate', '{imm}', '0x%02x'),
        )

    @property
    def address(self):
        for addr in (self.abs_addr, self.zp_addr, self.rel_addr, self.sp_addr):
            if addr is not None:
                return addr

    @property
    def target_address(self):
        # TODO does not know about sp_addr; see note about jsr \0xffaa in trace.py
        for addr in (self.rel_addr, self.abs_addr):
            if addr is not None:
                return addr

def disassemble_inst(memory, pc):
    opcode = Opcodes[memory[pc]]
    pc = (pc + 1) & 0xFFFF

    instlen = InstructionLengths[opcode.addr_mode]
    operands = bytearray()
    for i in range(instlen - 1):
        operands.append(memory[pc])
        pc = (pc + 1) & 0xFFFF

    inst = Instruction(
        disasm_template=opcode.disasm_template,
        addr_mode=opcode.addr_mode,
        opcode=opcode.number,
        flow_type=opcode.flow_type,
        operands=operands,
        )

    if inst.addr_mode in (AddressModes.Illegal,
                          AddressModes.Implied,
                          AddressModes.AccumulatorBit):
        pass

    elif inst.addr_mode in (AddressModes.Absolute,
                            AddressModes.AbsoluteX,
                            AddressModes.AbsoluteY,
                            AddressModes.IndirectAbsolute):
        inst.abs_addr = operands[0] + (operands[1] << 8)

    elif inst.addr_mode == AddressModes.Immediate:
        inst.immediate = operands[0]

    elif inst.addr_mode in (AddressModes.IndirectX,
                            AddressModes.ZeroPageIndirect,
                            AddressModes.ZeroPage,
                            AddressModes.ZeroPageBit,
                            AddressModes.ZeroPageX,
                            AddressModes.ZeroPageY,
                            AddressModes.IndirectY):
        inst.zp_addr = operands[0]

    elif inst.addr_mode == AddressModes.ZeroPageImmediate:
        inst.immediate = operands[0]
        inst.zp_addr = operands[1]

    elif inst.addr_mode == AddressModes.SpecialPage:
        inst.sp_addr = operands[0]

    elif inst.addr_mode in (AddressModes.Relative,
                            AddressModes.AccumulatorBitRelative):
        inst.rel_addr = _resolve_rel(pc, operands[0])

    elif inst.addr_mode in (AddressModes.Relative,
                            AddressModes.ZeroPageBitRelative):
        inst.zp_addr = operands[0]
        inst.rel_addr = _resolve_rel(pc, operands[1])

    else:
        msg = "Unhandled addressing mode %r at 0x%04x" % (
            inst.addr_mode, pc-1)
        raise NotImplementedError(msg) # always a bug

    return inst


def _resolve_rel(pc, displacement):
    if displacement & 0x80:
        displacement = -((displacement ^ 0xFF) + 1)
    return (pc + displacement) & 0xFFFF
