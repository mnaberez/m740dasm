all: clean out.bin

out.bin: out.lst
	python lst2bin.py out.lst out.bin

out.lst: testprog.asm
	as740 -l testprog.asm
	mv testprog.lst out.lst
	rm -f out.hlr

clean:
	rm -f out.*
