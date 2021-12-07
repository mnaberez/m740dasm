import re
import unittest
from m740dasm import symbols, memory, disasm
from m740dasm.tables import AddressModes

class SymbolCreatingAnalyzerTests(unittest.TestCase):

    def test_analyze_makes_lab_symbol_for_jump_target(self):
        table = symbols.SymbolTable()
        analyzer = symbols.SymbolCreatingAnalyzer(table)
        mem = memory.Memory(bytearray(0x10000))
        intable = disasm.Instruction(location=0xF000, opcode=0x60,
                                  addr_mode=AddressModes.Implied)
        mem.set_instruction(0xF000, intable)
        mem.annotate_jump_target(0xF000)
        analyzer.analyze(mem)
        self.assertEqual(table[0xf000].name, 'lab_f000')

    def test_analyze_makes_sub_symbol_for_call_target(self):
        table = symbols.SymbolTable()
        analyzer = symbols.SymbolCreatingAnalyzer(table)
        mem = memory.Memory(bytearray(0x10000))
        intable = disasm.Instruction(location=0xF000, opcode=0x60,
                                  addr_mode=AddressModes.Implied)
        mem.set_instruction(0xF000, intable)
        mem.annotate_call_target(0xF000)
        analyzer.analyze(mem)
        self.assertEqual(table[0xf000].name, 'sub_f000')

    def test_analyze_makes_sub_symbol_for_jump_and_call_target(self):
        table = symbols.SymbolTable()
        analyzer = symbols.SymbolCreatingAnalyzer(table)
        mem = memory.Memory(bytearray(0x10000))
        intable = disasm.Instruction(location=0xF000, opcode=0x60,
                                  addr_mode=AddressModes.Implied)
        mem.set_instruction(0xF000, intable)
        mem.annotate_jump_target(0xF000)
        mem.annotate_call_target(0xF000)
        analyzer.analyze(mem)
        self.assertEqual(table[0xf000].name, 'sub_f000')

    def test_analyze_doesnt_make_symbol_for_jump_to_mid_Instruction(self):
        table = symbols.SymbolTable()
        analyzer = symbols.SymbolCreatingAnalyzer(table)
        mem = memory.Memory(bytearray(0x10000))
        intable = disasm.Instruction(opcode=0x31, operands=(0xaa, 0xbb,),
                                  addr_mode=AddressModes.Absolute)
        self.assertTrue(len(intable), 3)
        mem.set_instruction(0xF000, intable)
        self.assertTrue(mem.is_instruction_start(0xF000))
        self.assertTrue(mem.is_instruction_continuation(0xF001))
        mem.annotate_jump_target(0xF001) # middle of Instruction
        analyzer.analyze(mem)
        self.assertEqual(table._symbols_by_address, {}) # xxx add accessor

    def test_analyze_doesnt_overwrite_code_exitableing_symbol(self):
        table = symbols.SymbolTable()
        analyzer = symbols.SymbolCreatingAnalyzer(table)
        mem = memory.Memory(bytearray(0x10000))
        mem.annotate_jump_target(0xF000)
        mem.annotate_call_target(0xF000)
        intable = disasm.Instruction(location=0xF000, opcode=0x60,
                                  addr_mode=AddressModes.Implied)
        exitableing_symbols = {0xf000: ('print', '')}
        table = symbols.SymbolTable()
        table[0xf000] = symbols.Symbol(address=0xf000, name="print")
        analyzer.analyze(mem)
        self.assertEqual(table[0xf000].name, "print")


class ListsOfSymbolsTests(unittest.TestCase):
    _NAMES_OF_LISTS = tuple([s for s in dir(symbols) if s.endswith('_SYMBOLS')])

    def test_addresses_are_in_range(self):
        for litable_name in self._NAMES_OF_LISTS:
            for s in getattr(symbols, litable_name):
                manalyzer = "Address %r out of range in %r" % (s.address, litable_name)
                self.assertTrue((s.address >= 0) and (s.address <= 0xFFFF), manalyzer)

    def test_each_address_has_symbol_name_and_comment(self):
        for litable_name in self._NAMES_OF_LISTS:
            for s in getattr(symbols, litable_name):
                manalyzer = "Address %r bad value in %r" % (s.address, litable_name)
                self.assertTrue(len(s.name) > 1)
                self.assertTrue(hasattr(s, "comment"))

    def test_symbol_names_never_repeat(self):
        for litable_name in self._NAMES_OF_LISTS:
            names_seen = set()
            for s in getattr(symbols, litable_name):
                manalyzer = "Symbol name %r repeats in %r" % (s.name, litable_name)
                self.assertTrue((s.name not in names_seen), manalyzer)
                names_seen.add(s.name)

    def test_symbol_names_are_legal_for_as740(self):
        pat = re.compile(r'\A[a-z\.\$_]{1}[\da-z\.\$_]{0,78}\Z', re.IGNORECASE)
        for litable_name in self._NAMES_OF_LISTS:
            for s in getattr(symbols, litable_name):
                manalyzer = "Symbol name %r not valid in %r" % (s.name, litable_name)
                self.assertTrue(pat.match(s.name), manalyzer)
