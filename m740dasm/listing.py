import struct

class Printer(object):
    def __init__(self, memory, start_address, symbol_table):
        self.memory = memory
        self.start_address = start_address
        self.symbol_table = symbol_table
        self.last_line_type = None

    def print_listing(self):
        self.print_header()
        self.print_symbols()

        address = self.start_address
        while address < len(self.memory):
            self.print_blank(address)
            self.print_label(address)

            if self.memory.is_instruction_start(address):
                inst = self.memory.get_instruction(address)
                self.print_instruction_line(address, inst)
                address += len(inst)
            else:
                if self.memory.is_vector_start(address):
                    self.print_vector_line(address)
                    address += 2
                elif self.memory.is_data(address):
                    self.print_data_line(address)
                    address += 1
                elif self.memory.is_unknown(address):
                    self.print_unknown_line(address)
                    address += 1
                else:
                    msg = "Unhandled location type %r at 0x%04x" % (
                        self.memory.types[address], address)
                    raise NotImplementedError(msg) # always a bug

    def print_header(self):
        print('    .area CODE1 (ABS)')
        print('    .org 0x%04x\n' % self.start_address)

    def print_symbols(self):
        used_symbols = set()
        for address, inst in self.memory.iter_instructions():
            if inst.data_ref_address in self.symbol_table:
                used_symbols.add(inst.data_ref_address)

        for address, target in self.memory.iter_vectors():
            if target in self.symbol_table:
                used_symbols.add(target)

        for address in sorted(used_symbols):
            if address < self.start_address:
                symbol = self.symbol_table[address]
                line = ("    %s = 0x%02x" % (symbol.name, symbol.address)).ljust(28)
                if symbol.comment:
                    line += ";%s" % symbol.comment
                print(line)
        print('')

    def print_blank(self, address):
        typ = self.memory.types[address]
        if self.last_line_type is not None:
            if typ != self.last_line_type:
                if address not in self.symbol_table:
                    print('')
        self.last_line_type = typ

    def print_label(self, address):
        if address in self.symbol_table:
            print("\n%s:" % self.format_abs_address(address))

    def print_data_line(self, address):
        self._print_byte_line(address, "DATA")

    def print_unknown_line(self, address):
        self._print_byte_line(address, "UNKNOWN")

    def _print_byte_line(self, address, tag):
        line = ('    .byte 0x%02x' % self.memory[address]).ljust(28)
        line += ';%04x  %02x          %s %s ' % (
            address,
            self.memory[address],
            tag,
            self._data_byte_repr(self.memory[address])
            )
        print(line)

    def _data_byte_repr(self, b):
        if (b >= 0x20) and (b <= 0x7e):  # printable 7-bit ascii
            return "0x%02x '%s'" % (b, chr(b))
        else:
            return "0x%02x" % b

    def print_vector_line(self, address):
        target = struct.unpack('<H', self.memory[address:address+2])[0]
        target = self.format_abs_address(target)
        line = ('    .word %s' % target).ljust(28)
        line += ';%04x  %02x %02x       VECTOR' % (address, self.memory[address], self.memory[address+1])
        if address in self.symbol_table:
            comment = self.symbol_table[address].comment
            if comment:
                line += ' ' + comment
        print(line)

    def print_mode_byte_line(self, address):
        line = ('    .byte 0x%02X' % self.memory[address]).ljust(28)
        line += ';%04x  %02x          MODE' % (address, self.memory[address])
        print(line)

    def print_reserved_byte_line(self, address):
        line = ('    .byte 0x%02X' % self.memory[address]).ljust(28)
        line += ';%04x  %02x          RESERVED' % (address, self.memory[address])
        print(line)

    def print_instruction_line(self, address, inst):
        disasm = inst.to_string(self.symbol_table)
        hexdump = (' '.join([ '%02x' % h for h in inst.all_bytes ])).ljust(9)

        line = '    ' + disasm.ljust(24)
        if not line.endswith(' '):
            line += ' '
        line += ';%04x  %s' % (address, hexdump)

        if inst.illegal:
            line += "Illegal instruction"

        print(line)

    def format_abs_address(self, address):
        if address in self.symbol_table:
            return self.symbol_table[address].name
        return '0x%04x' % address
