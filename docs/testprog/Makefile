all: clean out.bin

out.bin:
	cp -f testprog.asm out.asm
	as740 -l -o out.asm
	rm -f out.asm
	aslink out -i
	srec_cat out.ihx -intel -offset -0x8000 -o out.bin -binary

clean:
	rm -f out.*
