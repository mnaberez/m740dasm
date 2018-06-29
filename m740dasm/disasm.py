from m740dasm.tables import (
    AddressModes,
    Opcodes,
    InstructionLengths,
    )


class Instruction(object):
    __slots__ = ('disasm_template', 'addr_mode', 'opcode', 'operands',
                 'zp_addr', 'immediate', 'abs_addr', 'sp_addr', 'rel_addr')

    def __init__(self, **kwargs):
        self.disasm_template = '' # "cmp @ix+IXD, #IMB"
        self.addr_mode = None     # addressing mode
        self.zp_addr = None       # zero page address
        self.abs_addr = None      # absolute address
        self.sp_addr = None       # special page address
        self.rel_addr = None      # resolved relative address
        self.immediate = None     # immediate value
        self.opcode = None        # opcode byte
        self.operands = ()        # operand bytes

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

    _disasm_formats = (
        ('opcode',    '{opc}', '0x%02x'),
        ('zp_addr',   '{zp}',  '0x%02x'),
        ('sp_addr',   '{sp}',  '0xff%02x'),
        ('abs_addr',  '{abs}', '0x%04x'),
        ('rel_addr',  '{rel}', '0x%04x'),
        ('immediate', '{imm}', '0x%02x'),
        )


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

    else:
        msg = "Unhandled addressing mode %r at 0x%04x" % (
            inst.addr_mode, pc-1)
        raise NotImplementedError(msg) # always a bug

    return inst


def _resolve_rel(pc, displacement):
    if displacement & 0x80:
        displacement = -((displacement ^ 0xFF) + 1)
    return (pc + displacement) & 0xFFFF
