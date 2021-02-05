class SymbolTable(object):
    def __init__(self, initial_symbols=None):
        if initial_symbols is None:
            initial_symbols = {}
        self.symbols = initial_symbols.copy()

    def generate(self, memory, start_address):
        self.generate_code_symbols(memory, start_address)
        self.generate_data_symbols(memory, start_address)

    def generate_code_symbols(self, memory, start_address):
        for address in range(start_address, len(memory)):
            if address in self.symbols:
                pass # do not overwrite existing symbols
            elif memory.is_call_target(address):
                if memory.is_instruction_start(address):
                    self.symbols[address] = ('sub_%04x' % address, '')
            elif memory.is_jump_target(address):
                if memory.is_instruction_start(address):
                    self.symbols[address] = ('lab_%04x' % address, '')

    def generate_data_symbols(self, memory, start_address):
        for _, inst in memory.iter_instructions():
            address = inst.data_ref_address
            if address is None:
                continue
            if address in self.symbols:
                continue
            if memory.is_single_byte_or_start_of_multibyte(address):
                self.symbols[address] = ('mem_%04x' % address, '')

M3886_SYMBOLS = {
    # i/o
    0x0000: ("P0", 	    "Port P0"),
    0x0001: ("P0D",     "Port P0 direction register"),
    0x0002: ("P1", 	    "Port P1"),
    0x0003: ("P1D",     "Port P1 direction register"),
    0x0004: ("P2", 	    "Port P2"),
    0x0005: ("P2D",     "Port P2 direction register"),
    0x0006: ("P3", 	    "Port P3"),
    0x0007: ("P3D",     "Port P3 direction register"),
    0x0008: ("P4", 	    "Port P4"),
    0x0009: ("P4D",     "Port P4 direction register"),
    0x000a: ("P5", 	    "Port P5"),
    0x000b: ("P5D",     "Port P5 direction register"),
    0x000c: ("P6", 	    "Port P6"),
    0x000d: ("P6D",     "Port P6 direction register"),
    0x000e: ("P7", 	    "Port P7"),
    0x000f: ("P7D",     "Port P7 direction register"),
    0x0010: ("P8_P4I", 	"Port P8 / Port P4 input register"),
    0x0011: ("P8D_P7I", "Port P8 direction register / Port P7 input register"),
    0x0012: ("S0", 	    "I2C data shift register"),
    0x0013: ("S0D", 	"I2C address register"),
    0x0014: ("S1", 	    "I2C status register"),
    0x0015: ("S1D", 	"I2C control register"),
    0x0016: ("S2", 	    "I2C clock control register"),
    0x0017: ("S2D", 	"I2C start/stop condition control register"),
    0x0018: ("TB_RB", 	"Transmit/Receive buffer register"),
    0x0019: ("SIO1STS", "Serial I/O1 status register"),
    0x001a: ("SIO1CON", "Serial I/O1 control register"),
    0x001b: ("UARTCON", "UART control register"),
    0x001c: ("BRG", 	"Baud rate generator"),
    0x001d: ("SIO2CON", "Serial I/O2 control register"),
    0x001e: ("WDTCON", 	"Watchdog timer control register"),
    0x001f: ("SIO2", 	"Serial I/O2 register"),
    0x0020: ("PRE12", 	"Prescaler 12"),
    0x0021: ("T1", 	    "Timer 1"),
    0x0022: ("T2", 	    "Timer 2"),
    0x0023: ("TM", 	    "Timer XY mode register"),
    0x0024: ("PREX", 	"Prescaler X"),
    0x0025: ("TX", 	    "Timer X"),
    0x0026: ("PREY", 	"Prescaler Y"),
    0x0027: ("TY", 	    "Timer Y"),
    0x0028: ("DBB0", 	"Data bus buffer register 0"),
    0x0029: ("DBBSTS0", "Data bus buffer status register 0"),
    0x002a: ("DBBCON", 	"Data bus buffer control register"),
    0x002b: ("DBB1", 	"Data bus buffer register 1"),
    0x002c: ("DBBSTS1", "Data bus buffer status register 1"),
    0x002d: ("CMPD", 	"Comparator data register"),
    0x002e: ("PCTL1", 	"Port control register 1"),
    0x002f: ("PCTL2", 	"Port control register 2"),
    0x0030: ("PWM0H", 	"PWM0H register"),
    0x0031: ("PWM0L", 	"PWM0L register"),
    0x0032: ("PWM1H", 	"PWM1H register"),
    0x0033: ("PWM1L", 	"PWM1L register"),
    0x0034: ("ADCON", 	"AD/DA control register"),
    0x0035: ("AD1", 	"A-D conversion register 1"),
    0x0036: ("DA1", 	"D-A1 conversion register"),
    0x0037: ("DA2", 	"D-A2 conversion register"),
    0x0038: ("AD2", 	"A-D conversion register 2"),
    0x0039: ("INTSEL", 	"Interrupt source selection register"),
    0x003a: ("INTEDGE", "Interrupt edge selection register"),
    0x003b: ("CPUM", 	"CPU mode register"),
    0x003c: ("IREQ1", 	"Interrupt request register 1"),
    0x003d: ("IREQ2", 	"Interrupt request register 2"),
    0x003e: ("ICON1", 	"Interrupt control register 1"),
    0x003f: ("ICON2", 	"Interrupt control register 2"),
    0x0ffe: ("FCON", 	"Flash memory control register"),
    0x0fff: ("FCMD", 	"Flash command register"),

    # vectors
    0xfffc: ("RESET",    "Reset vector"),
    0xfffa: ("INT_FFFA", "INT0 / Input buffer full (IBF)"),
    0xfff8: ("INT_FFF8", "INT1 / Output buffer empty (OBE)"),
    0xfff6: ("INT_FFF6", "Serial I/O 1 reception"),
    0xfff4: ("INT_FFF4", "Serial I/O 2 transmission / SCL, SDA"),
    0xfff2: ("INT_FFF2", "Timer X"),
    0xfff0: ("INT_FFF0", "Timer Y"),
    0xffee: ("INT_FFEE", "Timer 1"),
    0xffec: ("INT_FFEC", "Timer 2"),
    0xffea: ("INT_FFEA", "CNTR0 / SCL, SDA"),
    0xffe8: ("INT_FFE8", "CNTR1 / Key-on wake-up"),
    0xffe6: ("INT_FFE6", "Serial I/O 2 / I2C"),
    0xffe4: ("INT_FFE4", "INT2 / I2C"),
    0xffe2: ("INT_FFE2", "INT3"),
    0xffe0: ("INT_FFE0", "INT4"),
    0xffde: ("INT_FFDE", "A-D converter / Key-on wake-up"),
    0xffdc: ("INT_BRK",  "BRK instruction interrupt"),
}
