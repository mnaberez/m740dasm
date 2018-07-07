import sys

from m740dasm.disasm import disassemble_inst
from m740dasm.trace import Tracer
from m740dasm.memory import Memory
from m740dasm.listing import Printer
from m740dasm.symbols import M3886_SYMBOLS, SymbolTable

def main():
    with open(sys.argv[1], 'rb') as f:
        rom = bytearray(f.read())
    start_address = 0x10000 - len(rom)

    memory = Memory(rom)

    entry_points = [0xc2eb,0x5a11,0x33e0,0x33ee,0x33f9,0x3405,0x3429,0x3435,0x3447,0x3458,
                    0xc31f,0xce8d,0xc9c3,0xc3e4,0xc40f,0xc446,0xc47e,0xc2c4,0xc4dd,0xc540,
                    0xc581,0xc5a1,0x5ab5,0x5ad5,0x5adf,0x5b16,0x5b1d,0x5b37,0x5b4a,0x5ce4,
                    0x5bbb,0x345c,0x3463,0x3466,0x3477,0x34a8,0x34b3,0x34d6,0x34d9,0x34e5,
                    0x7f7f,]

    vectors = [
        # brk
        0xffdc,
        # interrupts
        0xffde, 0xffe0, 0xffe2, 0xffe4, 0xffe6, 0xffe8, 0xffea, 0xffec,
        0xffee, 0xfff0, 0xfff2, 0xfff4, 0xfff6, 0xfff8, 0xfffa,
        # reset
        0xfffc,
    ]

    # 3570 - 3587 table of bytes for comparison
    for i in range(0x3588, 0x35b8, 2):
        vectors.append(i)

    for i in range(0x351e, 0x3570, 2):
        vectors.append(i)

    for i in range(0xb4db, 0xb50d, 2):
        vectors.append(i)

    # group reading handlers
    for i in range(0xa53a, 0xa54e, 2):
        vectors.append(i)

    traceable_range = range(start_address, start_address + len(rom) + 1)
    tracer = Tracer(memory, entry_points, vectors, traceable_range)
    tracer.trace(disassemble_inst)

    symbol_table = SymbolTable(M3886_SYMBOLS)
    symbol_table.generate(memory, start_address) # xxx should pass traceable_range

    printer = Printer(memory,
                      start_address,
                      symbol_table,
                      )
    printer.print_listing()


if __name__ == '__main__':
    main()
