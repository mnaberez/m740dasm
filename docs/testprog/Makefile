all: clean compare

compare: testprog.bin reassembled.bin
	diff testprog.bin reassembled.bin

clean:
	rm -f *.bin *.hlr *.ihx *.lst *.rel
	rm -f reassembled.asm

testprog.bin:
	as740 -l -o testprog.asm
	aslink testprog -i
	srec_cat testprog.ihx -intel -offset -0x8000 -o testprog.bin -binary

reassembled.bin: testprog.bin
	m740dasm testprog.bin > reassembled.asm
	as740 -l -o reassembled.asm
	aslink reassembled -i
	srec_cat reassembled.ihx -intel -offset -0x8000 -o reassembled.bin -binary
