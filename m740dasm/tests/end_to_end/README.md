# End-to-End tests

Running `make` will:

 - Assemble the test program with `as740`
 - Disassemble that binary with `m740dasm`
 - Assemble the disassembly with `as740`
 - Verify that the two binaries are identical

These programs must be installed and in `$PATH`:
 - `as740`
 - `srec_cat`
 - `m740dasm`
