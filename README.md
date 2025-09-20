# m740dasm

## Overview

m740dasm is a disassembler for Mitsubishi 740 binaries that generates output compatible with the [as740](http://shop-pdp.net/ashtml/as740.htm) assembler.  It can be used to disassemble firmware for many 8-bit Mitsubishi microcontrollers.  The 16- and 32-bit Mitsubishi microcontrollers use different instruction sets and are not supported.

m740dasm was developed to disassemble the firmware of the [Volkswagen Gamma V](https://github.com/mnaberez/vwradio) and [Volkswagen Rhapsody](https://github.com/mnaberez/vwradio) car radios made by TechniSat.  Both radios use the [M38869FFAHP](http://6502.org/documents/datasheets/mitsubishi/renesas_3886_group_users_manual.pdf) microcontroller.  

## Features

 - Identical Reassembly.  The assembly language output of m740dasm will assemble to a bit-for-bit exact copy of the original binary using as740.  This has been tested using several real firmware binaries and by fuzzing.

 - Code / Data Separation.  Starting from the vectors at the top of memory, m740dasm uses recursive traversal disassembly to separate code from data. This automates much of the disassembly process but indirect jumps will still need to be resolved manually.

 - Symbol Generation.  m740dasm tries not to write hardcoded addresses in the output when possible.  It will automatically add symbols for hardware registers and vectors, other memory locations used, and will add labels for branches and subroutines.

## Installation

m740dasm is written in Python and requires Python 3.8 or later.  You can download the package from this git repository and then install it into a virtual environment with:

```
$ git clone https://github.com/mnaberez/m740dasm.git
$ cd m740dasm
$ python3 -m venv ./venv
$ ./venv/bin/pip3 install --editable '.[test]'
```

After running the above, you can run the disassembler with `./venv/bin/m740dasm`
or run its unit tests with `./venv/bin/pytest`.

## Usage

m740dasm accepts a plain binary file as input.  The file is assumed to be a ROM image that should be aligned to the top of memory.  For example, if a 32K file is given, m740dasm will assume the image should be located at 0x8000-0xFFFF.  After loading the image, the disassembler reads the vectors at the top of memory and starts tracing instructions from there.

```
$ ./venv/bin/m740dasm input.bin > output.asm
```

The default MCU type is the `M3886` series.  Other types may be specified with the `-m` option, e.g. `-m M37450`.  Assuming the package was installed with `--editable` as shown above, you can add support for new devices by editing `devices.py`.

Most binaries will include some computed jumps, which m740dasm can't resolve on its own.  You can inform the disassembler of addresses containing code by adding them to the [`entry_points`](https://github.com/mnaberez/m740dasm/blob/9dd273a5230fcc265188e145cbda54c8db8afb29/m740dasm/command.py#L51-L52) list in `command.py`.

Once disassembled, the output file can be re-assembled to an identical binary using [as740](http://shop-pdp.net/ashtml/as740.htm).  A sample [`Makefile`](https://github.com/mnaberez/m740dasm/blob/bbf8d3f541e28c48cb05fe2fa6acc8fd8e1304fa/m740dasm/tests/end_to_end/Makefile) is included in this repository that shows the required as740 commands.

## Author

[Mike Naberezny](https://github.com/mnaberez)
