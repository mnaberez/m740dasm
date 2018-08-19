# m740dasm

## Overview

m740dasm is a disassembler for Mitsubishi 740 binaries that generates output compatible with the [as740](http://shop-pdp.net/ashtml/as740.htm) assembler.  It can be used to disassemble firmware for many 8-bit Mitsubishi microcontrollers.  The 16- and 32-bit Mitsubishi microcontrollers use different instruction sets and are not supported.

m740dasm was developed to disassemble the firmware of the [Volkswagen Gamma V](https://github.com/mnaberez/vwradio) car radio made by TechniSat.  This radio uses the [M38869FFAHP](http://6502.org/documents/datasheets/mitsubishi/renesas_3886_group_users_manual.pdf) microcontroller.  

## Features

 - Identical Reassembly.  The assembly language output of m740dasm will
   assemble to a bit-for-bit exact copy of the original binary using
   as740.  This has been tested using several real firmware binaries and
   by fuzzing.

 - Code / Data Separation.  Starting from the vectors at the top of memory,
   m740dasm uses recursive traversal disassembly to separate code from data.
   This automates much of the disassembly process but indirect jumps
   will still need to be resolved manually.

 - Symbol Generation.  m740dasm tries not to write hardcoded addresses in the
   output when possible.  It will automatically add symbols for hardware
   registers and vectors, other memory locations used, and will add labels for
   branches and subroutines.

## Installation

m740dasm is written in Python and requires Python 3.4 or later.  You can
download the package from this git repository and then install it with:

```
$ python setup.py install
```

## Usage

m740dasm accepts a plain binary file as input.  The file is assumed to be a
ROM image that should be aligned to the top of memory.  For example, if a
32K file is given, m740dasm will assume the image should be located at
0x8000-0xFFFF.  After loading the image, the disassembler reads the vectors
at the top of memory and starts tracing instructions from there.

```
$ m740dasm input.bin > output.asm
```

## Author

[Mike Naberezny](https://github.com/mnaberez)
