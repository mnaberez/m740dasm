
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


M3886_SYMBOLS = [
    # i/o
    Symbol(0x0000, "P0", 	    "Port P0"),
    Symbol(0x0001, "P0D",       "Port P0 direction register"),
    Symbol(0x0002, "P1", 	    "Port P1"),
    Symbol(0x0003, "P1D",       "Port P1 direction register"),
    Symbol(0x0004, "P2", 	    "Port P2"),
    Symbol(0x0005, "P2D",       "Port P2 direction register"),
    Symbol(0x0006, "P3", 	    "Port P3"),
    Symbol(0x0007, "P3D",       "Port P3 direction register"),
    Symbol(0x0008, "P4", 	    "Port P4"),
    Symbol(0x0009, "P4D",       "Port P4 direction register"),
    Symbol(0x000a, "P5", 	    "Port P5"),
    Symbol(0x000b, "P5D",       "Port P5 direction register"),
    Symbol(0x000c, "P6", 	    "Port P6"),
    Symbol(0x000d, "P6D",       "Port P6 direction register"),
    Symbol(0x000e, "P7", 	    "Port P7"),
    Symbol(0x000f, "P7D",       "Port P7 direction register"),
    Symbol(0x0010, "P8_P4I", 	"Port P8 / Port P4 input register"),
    Symbol(0x0011, "P8D_P7I",   "Port P8 direction register / Port P7 input register"),
    Symbol(0x0012, "S0", 	    "I2C data shift register"),
    Symbol(0x0013, "S0D", 	    "I2C address register"),
    Symbol(0x0014, "S1", 	    "I2C status register"),
    Symbol(0x0015, "S1D",       "I2C control register"),
    Symbol(0x0016, "S2", 	    "I2C clock control register"),
    Symbol(0x0017, "S2D",       "I2C start/stop condition control register"),
    Symbol(0x0018, "TB_RB", 	"Transmit/Receive buffer register"),
    Symbol(0x0019, "SIO1STS",   "Serial I/O1 status register"),
    Symbol(0x001a, "SIO1CON",   "Serial I/O1 control register"),
    Symbol(0x001b, "UARTCON",   "UART control register"),
    Symbol(0x001c, "BRG",       "Baud rate generator"),
    Symbol(0x001d, "SIO2CON",   "Serial I/O2 control register"),
    Symbol(0x001e, "WDTCON", 	"Watchdog timer control register"),
    Symbol(0x001f, "SIO2", 	    "Serial I/O2 register"),
    Symbol(0x0020, "PRE12", 	"Prescaler 12"),
    Symbol(0x0021, "T1", 	    "Timer 1"),
    Symbol(0x0022, "T2", 	    "Timer 2"),
    Symbol(0x0023, "TM", 	    "Timer XY mode register"),
    Symbol(0x0024, "PREX", 	    "Prescaler X"),
    Symbol(0x0025, "TX", 	    "Timer X"),
    Symbol(0x0026, "PREY", 	    "Prescaler Y"),
    Symbol(0x0027, "TY", 	    "Timer Y"),
    Symbol(0x0028, "DBB0", 	    "Data bus buffer register 0"),
    Symbol(0x0029, "DBBSTS0",   "Data bus buffer status register 0"),
    Symbol(0x002a, "DBBCON", 	"Data bus buffer control register"),
    Symbol(0x002b, "DBB1", 	    "Data bus buffer register 1"),
    Symbol(0x002c, "DBBSTS1",   "Data bus buffer status register 1"),
    Symbol(0x002d, "CMPD", 	    "Comparator data register"),
    Symbol(0x002e, "PCTL1", 	"Port control register 1"),
    Symbol(0x002f, "PCTL2", 	"Port control register 2"),
    Symbol(0x0030, "PWM0H", 	"PWM0H register"),
    Symbol(0x0031, "PWM0L", 	"PWM0L register"),
    Symbol(0x0032, "PWM1H", 	"PWM1H register"),
    Symbol(0x0033, "PWM1L", 	"PWM1L register"),
    Symbol(0x0034, "ADCON", 	"AD/DA control register"),
    Symbol(0x0035, "AD1", 	    "A-D conversion register 1"),
    Symbol(0x0036, "DA1", 	    "D-A1 conversion register"),
    Symbol(0x0037, "DA2", 	    "D-A2 conversion register"),
    Symbol(0x0038, "AD2", 	    "A-D conversion register 2"),
    Symbol(0x0039, "INTSEL", 	"Interrupt source selection register"),
    Symbol(0x003a, "INTEDGE",   "Interrupt edge selection register"),
    Symbol(0x003b, "CPUM", 	    "CPU mode register"),
    Symbol(0x003c, "IREQ1", 	"Interrupt request register 1"),
    Symbol(0x003d, "IREQ2", 	"Interrupt request register 2"),
    Symbol(0x003e, "ICON1", 	"Interrupt control register 1"),
    Symbol(0x003f, "ICON2", 	"Interrupt control register 2"),
    Symbol(0x0ffe, "FCON", 	    "Flash memory control register"),
    Symbol(0x0fff, "FCMD", 	    "Flash command register"),

    # vectors
    Symbol(0xfffc, "RESET",     "Reset vector"),
    Symbol(0xfffa, "INT_FFFA",  "INT0 / Input buffer full (IBF)"),
    Symbol(0xfff8, "INT_FFF8",  "INT1 / Output buffer empty (OBE)"),
    Symbol(0xfff6, "INT_FFF6",  "Serial I/O 1 reception"),
    Symbol(0xfff4, "INT_FFF4",  "Serial I/O 2 transmission / SCL, SDA"),
    Symbol(0xfff2, "INT_FFF2",  "Timer X"),
    Symbol(0xfff0, "INT_FFF0",  "Timer Y"),
    Symbol(0xffee, "INT_FFEE",  "Timer 1"),
    Symbol(0xffec, "INT_FFEC",  "Timer 2"),
    Symbol(0xffea, "INT_FFEA",  "CNTR0 / SCL, SDA"),
    Symbol(0xffe8, "INT_FFE8",  "CNTR1 / Key-on wake-up"),
    Symbol(0xffe6, "INT_FFE6",  "Serial I/O 2 / I2C"),
    Symbol(0xffe4, "INT_FFE4",  "INT2 / I2C"),
    Symbol(0xffe2, "INT_FFE2",  "INT3"),
    Symbol(0xffe0, "INT_FFE0",  "INT4"),
    Symbol(0xffde, "INT_FFDE",  "A-D converter / Key-on wake-up"),
    Symbol(0xffdc, "INT_BRK",   "BRK instruction interrupt"),
]
