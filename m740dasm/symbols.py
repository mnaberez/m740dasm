
class SymbolTable(object):
    """A mapping of addresses to Symbol objects"""

    def __init__(self, symbols=None):
        if symbols is None:
            symbols = []

        self._symbols_by_address = {}
        for symbol in symbols:
            self._symbols_by_address[symbol.address] = symbol

    def __contains__(self, address):
        return address in self._symbols_by_address

    def __getitem__(self, address):
        return self._symbols_by_address[address]

    def __setitem__(self, address, symbol):
        self._symbols_by_address[address] = symbol

    def analyze_symbols(self, memory):
        SymbolCreatingAnalyzer(self).analyze(memory)


class Symbol(object):
    """An address in memory along with its associated name and comment.
    If the symbol was not specified directly by the user, it is
    a "weak" symbol and may be changed or removed."""

    def __init__(self, address, name, comment='', weak=False):
        self.address   = address
        self.name      = name
        self.comment   = comment
        self.weak      = weak


class SymbolCreatingAnalyzer(object):
    """Given a SymbolTable and Memory, analyze the code and then populate
    the symbol table with weak symbols for code and data."""

    def __init__(self, symbol_table):
        self._symbol_table = symbol_table

    def analyze(self, memory):
        self._analyze_entry_point_symbols(memory)
        self._analyze_code_symbols(memory)
        self._analyze_data_symbols(memory)

    def _analyze_entry_point_symbols(self, memory):
        """analyze symbols for addresses known to contain code but are
        not the targets of jump or call instructions."""
        for address, inst in memory.iter_instructions():
            if not self._can_set_symbol(address):
                continue
            if memory.is_entry_point(address):
                self._set_weak_symbol(address, _Prefixes.Label)

    def _analyze_code_symbols(self, memory):
        """analyze symbols for jump and call targets."""
        for address, inst in memory.iter_instructions():
            if not self._can_set_symbol(address):
                continue
            elif not memory.is_instruction_start(address):
                continue
            elif memory.is_call_target(address):
                self._set_weak_symbol(address, _Prefixes.Subroutine)
            elif memory.is_jump_target(address):
                self._set_weak_symbol(address, _Prefixes.Label)

    def _analyze_data_symbols(self, memory):
        """analyze symbols for memory used in data operations."""
        for _, inst in memory.iter_instructions():
            address = inst.data_ref_address
            if address is None:
                continue
            if not self._can_set_symbol(address):
                continue
            if memory.is_instruction_start(address):
                if address in self._symbol_table:
                    continue # do not overwrite a weak code symbol
            if memory.is_single_byte_or_start_of_multibyte(address):
                self._set_weak_symbol(address, _Prefixes.Memory)

    def _can_set_symbol(self, address):
        """A symbol can be set if one is not there, or if a weak one
        is there.  User-provided symbols are never overwritten."""
        if address not in self._symbol_table:
            return True
        return self._symbol_table[address].weak

    def _set_weak_symbol(self, address, prefix):
        """Set a "weak" symbol at the address."""
        name = "%s_%04x" % (prefix, address)
        symbol = Symbol(address, name, comment='', weak=True)
        self._symbol_table[address] = symbol


class _Prefixes:
    Label =      "lab"
    Subroutine = "sub"
    Memory =     "mem"

