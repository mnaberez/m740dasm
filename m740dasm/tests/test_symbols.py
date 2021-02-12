import re
import unittest
from m740dasm import symbols, memory, disasm
from m740dasm.tables import AddressModes

class SymbolGeneratorTests(unittest.TestCase):

    def test_generate_makes_lab_symbol_for_jump_target(self):
        st = symbols.SymbolTable()
        sg = symbols.SymbolGenerator(st)
        mem = memory.Memory(bytearray(0x10000))
        inst = disasm.Instruction(location=0xF000, opcode=0x60,
                                  addr_mode=AddressModes.Implied)
        mem.set_instruction(0xF000, inst)
        mem.annotate_jump_target(0xF000)
        sg.generate(mem)
        self.assertEqual(st[0xf000].name, 'lab_f000')

    def test_generate_makes_sub_symbol_for_call_target(self):
        st = symbols.SymbolTable()
        sg = symbols.SymbolGenerator(st)
        mem = memory.Memory(bytearray(0x10000))
        inst = disasm.Instruction(location=0xF000, opcode=0x60,
                                  addr_mode=AddressModes.Implied)
        mem.set_instruction(0xF000, inst)
        mem.annotate_call_target(0xF000)
        sg.generate(mem)
        self.assertEqual(st[0xf000].name, 'sub_f000')

    def test_generate_makes_sub_symbol_for_jump_and_call_target(self):
        st = symbols.SymbolTable()
        sg = symbols.SymbolGenerator(st)
        mem = memory.Memory(bytearray(0x10000))
        inst = disasm.Instruction(location=0xF000, opcode=0x60,
                                  addr_mode=AddressModes.Implied)
        mem.set_instruction(0xF000, inst)
        mem.annotate_jump_target(0xF000)
        mem.annotate_call_target(0xF000)
        sg.generate(mem)
        self.assertEqual(st[0xf000].name, 'sub_f000')

    def test_generate_doesnt_make_symbol_for_jump_to_mid_instruction(self):
        st = symbols.SymbolTable()
        sg = symbols.SymbolGenerator(st)
        mem = memory.Memory(bytearray(0x10000))
        inst = disasm.Instruction(opcode=0x31, operands=(0xaa, 0xbb,),
                                  addr_mode=AddressModes.Absolute)
        self.assertTrue(len(inst), 3)
        mem.set_instruction(0xF000, inst)
        self.assertTrue(mem.is_instruction_start(0xF000))
        self.assertTrue(mem.is_instruction_continuation(0xF001))
        mem.annotate_jump_target(0xF001) # middle of instruction
        sg.generate(mem)
        self.assertEqual(st._symbols_by_address, {}) # xxx add accessor

    def test_generate_doesnt_overwrite_code_existing_symbol(self):
        st = symbols.SymbolTable()
        sg = symbols.SymbolGenerator(st)
        mem = memory.Memory(bytearray(0x10000))
        mem.annotate_jump_target(0xF000)
        mem.annotate_call_target(0xF000)
        inst = disasm.Instruction(location=0xF000, opcode=0x60,
                                  addr_mode=AddressModes.Implied)
        existing_symbols = {0xf000: ('print', '')}
        st = symbols.SymbolTable()
        st[0xf000] = symbols.Symbol(address=0xf000, name="print")
        sg.generate(mem)
        self.assertEqual(st[0xf000].name, "print")


class SymbolListsTests(unittest.TestCase):
    def test_addresses_are_in_range(self):
        for list_name in _NAMES_OF_LISTS:
            for s in getattr(symbols, list_name):
                msg = "Address %r out of range in %r" % (s.address, list_name)
                self.assertTrue((s.address >= 0) and (s.address <= 0xFFFF), msg)

    def test_each_address_has_symbol_name_and_comment(self):
        for list_name in _NAMES_OF_LISTS:
            for s in getattr(symbols, list_name):
                msg = "Address %r bad value in %r" % (s.address, list_name)
                self.assertTrue(len(s.name) > 1)
                self.assertTrue(hasattr(s, "comment"))

    def test_symbol_names_never_repeat(self):
        for list_name in _NAMES_OF_LISTS:
            names_seen = set()
            for s in getattr(symbols, list_name):
                msg = "Symbol name %r repeats in %r" % (s.name, list_name)
                self.assertTrue((s.name not in names_seen), msg)
                names_seen.add(s.name)

    def test_symbol_names_are_legal_for_as740(self):
        pat = re.compile(r'\A[a-z\.\$_]{1}[\da-z\.\$_]{0,78}\Z', re.IGNORECASE)
        for list_name in _NAMES_OF_LISTS:
            for s in getattr(symbols, list_name):
                msg = "Symbol name %r not valid in %r" % (s.name, list_name)
                self.assertTrue(pat.match(s.name), msg)


_NAMES_OF_LISTS = [s for s in dir(symbols) if s.endswith('_SYMBOLS')]
