'''
Usage: m740dasm <filename.bin>

'''

import sys

from m740dasm.disasm import disassemble
from m740dasm.trace import Tracer
from m740dasm.memory import Memory
from m740dasm.listing import Printer
from m740dasm.symbols import SymbolTable
from m740dasm.devices import Devices

def main():
    if len(sys.argv) != 2:
        sys.stderr.write(__doc__)
        sys.exit(1)

    with open(sys.argv[1], 'rb') as f:
        rom = bytearray(f.read())
    start_address = 0x10000 - len(rom)

    selected_device = "M3886"

    memory = Memory(rom)

    # addresses known to contain code
    entry_points = [
    ]

    # address of hardware vectors or other locations that contain
    # a 2-byte address of code
    vectors = Devices[selected_device]["vector_table"]

    traceable_range = range(start_address, start_address + len(rom) + 1)
    tracer = Tracer(memory, entry_points, vectors, traceable_range)
    tracer.trace(disassemble)

    symbol_table = SymbolTable(Devices[selected_device]["symbol_table"])
    symbol_table.analyze_symbols(memory)

    printer = Printer(memory,
                      start_address,
                      symbol_table,
                      )
    printer.print_listing()


if __name__ == '__main__':
    main()
