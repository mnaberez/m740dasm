'''
Usage: m740dasm [-m MCUtype] <filename.bin>

'''

import sys, getopt

from m740dasm.disasm import disassemble
from m740dasm.trace import Tracer
from m740dasm.memory import Memory
from m740dasm.listing import Printer
from m740dasm.symbols import SymbolTable
from m740dasm.devices import Devices

def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hm:",["help","mcutype="])
    except getopt.GetoptError:
        sys.stderr.write(__doc__)
        sys.exit(1)

    default_device  = "M3886"
    selected_device = default_device

    for opt, val in opts:
        if opt in ("-h", "--help"):
            print(__doc__)
            sys.exit(0)
        elif opt in ("-m", "--mcutype"):
            if val not in Devices.keys():
                sys.stderr.write("Unsupported MCU type requested (%s)! Currently supported: %s\n"%(val, ', '.join(Devices.keys())))
                sys.exit(2)
            else:
                selected_device = val
        else:
            sys.stderr.write(__doc__)
            sys.exit(1)

    if len(args) == 0:
        sys.stderr.write(__doc__)
        sys.exit(1)

    with open(args[0], 'rb') as f:
        rom = bytearray(f.read())
    start_address = 0x10000 - len(rom)

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
