import sys
import unittest
from m740dasm.disasm import disassemble_inst
from m740dasm.tables import AddressModes


class disassemble_inst_tests(unittest.TestCase):
    # brk                 ;00         Implied
    def test_00_brk(self):
        mem = [0x00]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "brk")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # ora [0xaa,x]        ;01 aa      Indirect X
    def test_01_ora(self):
        mem = [0x01, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ora [0xaa,x]")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # jsr [0xaa]          ;02 aa      Zero Page Indirect
    def test_01_jsr(self):
        mem = [0x02, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "jsr [0xaa]")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageIndirect)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bbs 0,a,label4      ;03 fe      Accumulator Bit Relative
    def test_03_bbs(self):
        mem = [0x03, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbs 0,a,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBitRelative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # .byte 0x04          ;04         Illegal
    def test_04_illegal(self):
        mem = [0x04]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x04")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # ora 0xaa            ;05 aa      Zero Page
    def test_05_ora(self):
        mem = [0x05, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ora 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # asl 0x45            ;06 45      Zero Page
    def test_06_asl(self):
        mem = [0x06, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "asl 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bbs 0,0xaa,label5   ;07 aa fd   Zero Page Bit Relative
    def test_07_bbs(self):
        mem = [0x07, 0xaa, 0x1d]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbs 0,0xaa,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBitRelative)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # php                 ;08         Implied
    def test_08_php(self):
        mem = [0x08]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "php")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # ora #0xaa           ;09 aa      Immediate
    def test_09_ora(self):
        mem = [0x09, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ora #0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Immediate)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # asl a               ;0a         Implied
    def test_0a_asl(self):
        mem = [0x0a]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "asl a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # seb 0,a             ;0b         Accumulator Bit
    def test_0b_seb(self):
        mem = [0x0b]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 0,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # .byte 0x0c          ;0c         Illegal
    def test_0c_illegal(self):
        mem = [0x0c]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x0c")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # ora 0xaabb          ;0d bb aa   Absolute
    def test_0d_ora(self):
        mem = [0x0d, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ora 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # asl 0xaabb          ;0e bb aa   Absolute
    def test_0e_abs(self):
        mem = [0x0e, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "asl 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # seb 0,0xaa          ;0f aa      Zero Page Bit
    def test_0f_seb(self):
        mem = [0x0f, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 0,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bpl label6          ;10 fe      Relative
    def test_10_bpl(self):
        mem = [0x10, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bpl 0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Relative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # ora [0xaa],y        ;11 aa      Indirect Y
    def test_11_ora(self):
        mem = [0x11, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ora [0xaa],y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectY)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # clt                 ;12         Implied
    def test_12_clt(self):
        mem = [0x12]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clt")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # bbc 0,a,label7      ;13 fe      Accumulator Bit Relative
    def test_13_bbc(self):
        mem = [0x13, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbc 0,a,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBitRelative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # .byte 0x14          ;14         Illegal
    def test_14_illegal(self):
        mem = [0x14]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x14")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # ora 0xaa,x          ;15 aa      Zero Page X
    def test_15_ora(self):
        mem = [0x15, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ora 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # asl 0xaa,x          ;16 aa      Zero Page X
    def test_16_asl(self):
        mem = [0x16, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "asl 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)
        self.assertEqual(inst.data_ref_address, 0xaa)
        self.assertEqual(inst.code_ref_address, None)

    # bbc 0,0xaa,label8   ;17 aa fd   Zero Page Bit Relative
    def test_17_bbc(self):
        mem = [0x17, 0xaa, 0x1d]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbc 0,0xaa,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBitRelative)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # clc                 ;18         Implied
    def test_18_clc(self):
        mem = [0x18]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clc")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # ora 0xaabb,y        ;19 bb aa   Absolute Y
    def test_19_ora(self):
        mem = [0x19, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ora 0xaabb,y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteY)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # dec a               ;1a         Implied
    def test_1a_dec(self):
        mem = [0x1a]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "dec a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # clb 0,a             ;1b         Accumulator Bit
    def test_1b_clb(self):
        mem = [0x1b]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 0,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # .byte 0x1c          ;1c         Illegal
    def test_1c_illegal(self):
        mem = [0x1c]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x1c")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # ora 0xaabb,x        ;1d bb aa   Absolute X
    def test_1d_ora(self):
        mem = [0x1d, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ora 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # asl 0xaabb,x        ;1e bb aa   Absolute X
    def test_1e_asl(self):
        mem = [0x1e, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "asl 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # clb 0,0xaa          ;1f aa      Zero Page Bit
    def test_1f_clb(self):
        mem = [0x1f, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 0,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # jsr 0xaabb          ;20 bb aa   Absolute
    def test_20_jsr(self):
        mem = [0x20, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "jsr 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0xaabb)

    # and [0xaa,x]        ;21 aa      Indirect X
    def test_21_and(self):
        mem = [0x21, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "and [0xaa,x]")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # jsr \0xffaa         ;22         Special Page
    def test_22_jsr(self):
        mem = [0x22, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "jsr \\0xffaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.SpecialPage)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0xffaa)

    # bbs 1,a,label9      ;23 fe      Accumulator Bit Relative
    def test_23_bbs(self):
        mem = [0x23, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbs 1,a,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBitRelative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # bit 0xaa            ;24 aa      Zero Page
    def test_24_bit(self):
        mem = [0x24, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bit 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # and 0xaa            ;25 aa      Zero Page
    def test_25_and(self):
        mem = [0x25, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "and 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # rol 0xaa            ;26 aa      Zero Page
    def test_26_rol(self):
        mem = [0x26, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "rol 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bbs 1,0xaa,label10  ;27 aa fd   Zero Page Bit Relative
    def test_27_bbs(self):
        mem = [0x27, 0xaa, 0x1d]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbs 1,0xaa,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBitRelative)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # plp                 ;28         Implied
    def test_28_plp(self):
        mem = [0x28]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "plp")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # and #0xaa           ;29 aa      Immediate
    def test_29_plp(self):
        mem = [0x29, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "and #0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Immediate)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # rol a               ;2a         Implied
    def test_2a_rol(self):
        mem = [0x2a]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "rol a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # seb 1,a             ;2b         Accumulator Bit
    def test_2b_seb(self):
        mem = [0x2b]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 1,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # bit 0xaabb          ;2c bb aa   Absolute
    def test_2c_bit(self):
        mem = [0x2c, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bit 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # and 0xaabb          ;2d bb aa   Absolute
    def test_2d_and(self):
        mem = [0x2d, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "and 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # rol 0xaabb          ;2e bb aa   Absolute
    def test_2e_rol(self):
        mem = [0x2e, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "rol 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # seb 1,0xaa          ;2f aa      Zero Page Bit
    def test_2f_seb(self):
        mem = [0x2f, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 1,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)
        self.assertEqual(inst.data_ref_address, 0xaa)
        self.assertEqual(inst.code_ref_address, None)

    # bmi label11         ;30 fe      Relative
    def test_30_bmi(self):
        mem = [0x30, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bmi 0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Relative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # and [0xaa],y        ;31 aa      Indirect Y
    def test_31_and(self):
        mem = [0x31, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "and [0xaa],y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectY)
        self.assertEqual(inst.data_ref_address, 0xAA)
        self.assertEqual(inst.code_ref_address, None)

    # set                 ;32         Implied
    def test_32_set(self):
        mem = [0x32]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "set")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # bbc 1,a,label12     ;33 fe      Accumulator Bit Relative
    def test_33_bbc(self):
        mem = [0x33, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbc 1,a,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBitRelative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # .byte 0x34          ;34 00      Illegal
    def test_34_illegal(self):
        mem = [0x34]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x34")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # and 0xaa,x          ;35 aa      Zero Page X
    def test_35_and(self):
        mem = [0x35, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "and 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # rol 0xaa,x          ;36 aa      Zero Page X
    def test_36_rol(self):
        mem = [0x36, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "rol 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bbc 1,0xaa,label13  ;37 aa fd   Zero Page Bit Relative
    def test_37_bbc(self):
        mem = [0x37, 0xaa, 0x1d]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbc 1,0xaa,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBitRelative)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # sec                 ;38         Implied
    def test_38_sec(self):
        mem = [0x38]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sec")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # and 0xaabb,y        ;39 bb aa   Absolute Y
    def test_39_and(self):
        mem = [0x39, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "and 0xaabb,y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteY)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # inc a               ;3a         Implied
    def test_3a_inc(self):
        mem = [0x3a]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "inc a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # ldm #0xaa,0xbb      ;3c aa bb   Zero Page Immediate
    def test_3c_ldm(self):
        mem = [0x3c, 0xaa, 0xbb]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ldm #0xaa,0xbb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageImmediate)
        self.assertEqual(inst.data_ref_address, 0x00bb)
        self.assertEqual(inst.code_ref_address, None)

    # and 0xaabb,x        ;3d bb aa   Absolute X
    def test_3d_and(self):
        mem = [0x3d, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "and 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # rol 0xaabb,x        ;3e bb aa   Absolute X
    def test_3e_rol(self):
        mem = [0x3e, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "rol 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # clb 1,0xaa          ;3f aa      Zero Page Bit
    def test_3f_clb(self):
        mem = [0x3f, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 1,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)
        self.assertEqual(inst.data_ref_address, 0xaa)
        self.assertEqual(inst.code_ref_address, None)

    # rti                 ;40         Implied
    def test_40_rti(self):
        mem = [0x40]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "rti")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # eor [0xaa,x]        ;41 aa      Indirect X
    def test_41_eor(self):
        mem = [0x41, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "eor [0xaa,x]")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # stp                 ;42         Implied
    def test_42_stp(self):
        mem = [0x42]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "stp")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # bbs 2,a,label14     ;43 fe      Accumulator Bit Relative
    def test_43_bbs(self):
        mem = [0x43, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbs 2,a,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBitRelative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # com 0xaa            ;44 aa      Zero Page
    def test_44_com(self):
        mem = [0x44, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "com 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # eor 0xaa            ;45 aa      Zero Page
    def test_45_eor(self):
        mem = [0x45, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "eor 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # lsr 0xaa            ;46 aa      Zero Page
    def test_46_lsr(self):
        mem = [0x46, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "lsr 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bbs 2,0xaa,label15  ;47 aa fd   Zero Page Bit Relative
    def test_47_bbs(self):
        mem = [0x47, 0xaa, 0x1d]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbs 2,0xaa,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBitRelative)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # pha                 ;48         Implied
    def test_48_pha(self):
        mem = [0x48]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "pha")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # eor #0xaa           ;49 aa      Immediate
    def test_49_eor(self):
        mem = [0x49, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "eor #0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Immediate)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # lsr a               ;4a         Implied
    def test_4a_lsr(self):
        mem = [0x4a]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "lsr a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # seb 2,a             ;4b         Accumulator Bit
    def test_4b_seb(self):
        mem = [0x4b]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 2,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # jmp 0xaabb          ;4c bb aa   Absolute
    def test_4c_jmp(self):
        mem = [0x4c, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "jmp 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0xaabb)

    # eor 0xaabb          ;4d bb aa   Absolute
    def test_4d_eor(self):
        mem = [0x4d, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "eor 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # lsr 0xaabb          ;4e bb aa   Absolute
    def test_4e_lsr(self):
        mem = [0x4e, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "lsr 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # seb 2,0xaa          ;4f aa      Zero Page Bit
    def test_4f_seb(self):
        mem = [0x4f, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 2,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bvc label16         ;50 fe      Relative
    def test_50_bvc(self):
        mem = [0x50, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bvc 0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Relative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # eor [0xaa],y        ;51 aa      Indirect Y
    def test_51_eor(self):
        mem = [0x51, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "eor [0xaa],y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectY)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # .byte 0x52          ;52         Illegal
    def test_52_illegal(self):
        mem = [0x52]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x52")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # bbc 2,a,label17     ;53 fe      Accumulator Bit Relative
    def test_53_bbc(self):
        mem = [0x53, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbc 2,a,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBitRelative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # .byte 0x54          ;54         Illegal
    def test_54_illegal(self):
        mem = [0x54]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x54")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # eor 0xaa,x          ;55 aa      Zero Page X
    def test_55_eor(self):
        mem = [0x55, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "eor 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # lsr 0xaa,x          ;56 aa      Zero Page X
    def test_56_lsr(self):
        mem = [0x56, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "lsr 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bbc 2,0xaa,label18  ;57 aa fd   Zero Page Bit Relative
    def test_57_bbc(self):
        mem = [0x57, 0xaa, 0x1d]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbc 2,0xaa,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBitRelative)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # cli                 ;58         Implied
    def test_58_cli(self):
        mem = [0x58]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "cli")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # eor 0xaabb,y        ;59 bb aa   Absolute Y
    def test_59_eor(self):
        mem = [0x59, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "eor 0xaabb,y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteY)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # .byte 0x5a          ;5a         Illegal
    def test_5a_illegal(self):
        mem = [0x5a]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x5a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # clb 2,a             ;5b         Accumulator Bit
    def test_5b_clb(self):
        mem = [0x5b]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 2,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # .byte 0x5c          ;5c         Illegal
    def test_5c_illegal(self):
        mem = [0x5c]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x5c")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # eor 0xaabb,x        ;5d bb aa   Absolute X
    def test_5d_eor(self):
        mem = [0x5d, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "eor 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # lsr 0xaabb,x        ;5e bb aa   Absolute X
    def test_5e_lsr(self):
        mem = [0x5e, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "lsr 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # clb 2,0xaa          ;5f aa      Zero Page Bit
    def test_5f_clb(self):
        mem = [0x5f, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 2,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # rts                 ;60         Implied
    def test_60_rts(self):
        mem = [0x60]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "rts")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # adc [0xaa,x]        ;61 aa      Indirect X
    def test_61_adc(self):
        mem = [0x61, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "adc [0xaa,x]")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # mul 0xaa,x          ;62 aa      Zero Page X
    def test_62_mul(self):
        mem = [0x62, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "mul 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bbs 3,a,label19     ;63 fe      Accumulator Bit Relative
    def test_63_bbs(self):
        mem = [0x63, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbs 3,a,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBitRelative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # tst 0xaa            ;64 aa      Zero Page
    def test_64_tst(self):
        mem = [0x64, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "tst 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # adc 0xaa            ;65 aa      Zero Page
    def test_65_adc(self):
        mem = [0x65, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "adc 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # ror 0xaa            ;66 aa      Zero Page
    def test_66_ror(self):
        mem = [0x66, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ror 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bbs 3,0xaa,label20  ;67 aa fd   Zero Page Bit Relative
    def test_67_bbs(self):
        mem = [0x67, 0xaa, 0x1d]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbs 3,0xaa,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBitRelative)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # pla                 ;68         Implied
    def test_68_pla(self):
        mem = [0x68]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "pla")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # adc #0xaa           ;69 aa      Immediate
    def test_69_adc(self):
        mem = [0x69, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "adc #0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Immediate)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # ror a               ;6a         Implied
    def test_6a_ror(self):
        mem = [0x6a]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ror a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # seb 3,a             ;6b         Accumulator Bit
    def test_6b_seb(self):
        mem = [0x6b]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 3,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # jmp [0xaabb]        ;6c bb aa   Indirect Absolute
    def test_6c_jmp(self):
        mem = [0x6c, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "jmp [0xaabb]")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectAbsolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # adc 0xaabb          ;6d bb aa   Absolute
    def test_6d_adc(self):
        mem = [0x6d, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "adc 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # ror 0xaabb          ;6e bb aa   Absolute
    def test_6e_ror(self):
        mem = [0x6e, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ror 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # seb 3,0xaa          ;6f aa      Zero Page Bit
    def test_6f_seb(self):
        mem = [0x6f, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 3,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bvs label21         ;70 fe      Relative
    def test_70_bvs(self):
        mem = [0x70, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bvs 0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Relative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # adc [0xaa],y        ;71 aa      Indirect Y
    def test_71_adc(self):
        mem = [0x71, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "adc [0xaa],y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectY)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # .byte 0x72          ;72         Illegal
    def test_72_illegal(self):
        mem = [0x72]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x72")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # bbc 3,a,label22     ;73 fe      Accumulator Bit Relative
    def test_73_bbc(self):
        mem = [0x73, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbc 3,a,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBitRelative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # .byte 0x74          ;74         Illegal
    def test_74_illegal(self):
        mem = [0x74]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x74")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # adc 0xaa,x          ;75 aa      Zero Page X
    def test_75_adc(self):
        mem = [0x75, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "adc 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # ror 0xaa,x          ;76 aa      Zero Page X
    def test_76_ror(self):
        mem = [0x76, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ror 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bbc 3,0xaa,label23  ;77 aa fd   Zero Page Bit Relative
    def test_77_bbc(self):
        mem = [0x77, 0xaa, 0x1d]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbc 3,0xaa,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBitRelative)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # sei                 ;78         Implied
    def test_78_sei(self):
        mem = [0x78]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sei")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # adc 0xaabb,y        ;79 bb aa   Absolute Y
    def test_79_adc(self):
        mem = [0x79, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "adc 0xaabb,y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteY)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # .byte 0x7a          ;7a         Illegal
    def test_7a_illegal(self):
        mem = [0x7a]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x7a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # clb 3,a             ;7b         Accumulator Bit
    def test_7b_clb(self):
        mem = [0x7b]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 3,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # .byte 0x7a          ;7c         Illegal
    def test_7c_illegal(self):
        mem = [0x7c]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x7c")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # adc 0xaabb,x        ;7d bb aa   Absolute X
    def test_7d_adc(self):
        mem = [0x7d, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "adc 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # ror 0xaabb,x        ;7e bb aa   Absolute X
    def test_7e_ror(self):
        mem = [0x7e, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ror 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # clb 3,0xaa          ;7f aa      Zero Page Bit
    def test_7f_clb(self):
        mem = [0x7f, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 3,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bra label24         ;80 fe      Relative
    def test_80_bra(self):
        mem = [0x80, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bra 0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Relative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # sta [0xaa,x]        ;81 aa      Indirect X
    def test_81_sta(self):
        mem = [0x81, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sta [0xaa,x]")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # rrf 0xaa            ;82 aa      Zero Page
    def test_rrf_aa(self):
        mem = [0x82, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "rrf 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bbs 4,a,label25     ;83 fe      Accumulator Bit Relative
    def test_83_bbs(self):
        mem = [0x83, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbs 4,a,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBitRelative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # sty 0xaa            ;84 aa      Zero Page
    def test_84_sty(self):
        mem = [0x84, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sty 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # sta 0xaa            ;85 aa      Zero Page
    def test_85_sta(self):
        mem = [0x85, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sta 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # stx 0xaa            ;86 aa      Zero Page
    def test_86_stx(self):
        mem = [0x86, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "stx 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bbs 4,0xaa,label26  ;87 aa fd   Zero Page Bit Relative
    def test_87_bbs(self):
        mem = [0x87, 0xaa, 0x1d]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbs 4,0xaa,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBitRelative)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # dey                 ;88         Implied
    def test_88_dey(self):
        mem = [0x88]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "dey")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # .byte 0x89          ;89         Illegal
    def test_89_illegal(self):
        mem = [0x89]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x89")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # txa                 ;8a         Implied
    def test_8a_txa(self):
        mem = [0x8a]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "txa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # seb 4,a             ;8b         Accumulator Bit
    def test_8b_seb(self):
        mem = [0x8b]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 4,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # sty 0xaabb          ;8c bb aa   Absolute
    def test_8c_sty(self):
        mem = [0x8c, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sty 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # sta 0xaabb          ;8d bb aa   Absolute
    def test_8d_sta(self):
        mem = [0x8d, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sta 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # stx 0xaabb          ;8e bb aa   Absolute
    def test_8e_stx(self):
        mem = [0x8e, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "stx 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # seb 4,0xaa          ;8f aa      Zero Page Bit
    def test_8f_seb(self):
        mem = [0x8f, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 4,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bcc label27         ;90 fe      Relative
    def test_90_bcc(self):
        mem = [0x90, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bcc 0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Relative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # sta [0xaa],y        ;91 aa      Indirect Y
    def test_91_sta(self):
        mem = [0x91, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sta [0xaa],y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectY)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # .byte 0x92          ;92         Illegal
    def test_92_illegal(self):
        mem = [0x92]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x92")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # bbc 4,a,label28     ;93 fe      Accumulator Bit Relative
    def test_93_bbc(self):
        mem = [0x93, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbc 4,a,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBitRelative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # sty 0xaa,x          ;94 aa      Zero Page X
    def test_94_sty(self):
        mem = [0x94, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sty 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # sta 0xaa,x          ;95 aa      Zero Page X
    def test_95_sta(self):
        mem = [0x95, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sta 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # stx 0xaa,y          ;96 aa      Zero Page Y
    def test_96_stx(self):
        mem = [0x96, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "stx 0xaa,y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageY)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bbc 4,0xaa,label29  ;97 aa fd   Zero Page Bit Relative
    def test_97_bbc(self):
        mem = [0x97, 0xaa, 0x1d]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbc 4,0xaa,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBitRelative)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # tya                 ;98         Implied
    def test_98_tya(self):
        mem = [0x98]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "tya")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # sta 0xaabb,y        ;99 bb aa   Absolute Y
    def test_99_sta(self):
        mem = [0x99, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sta 0xaabb,y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteY)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # txs                 ;9a         Implied
    def test_9a_txs(self):
        mem = [0x9a]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "txs")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # clb 4,a             ;9b         Accumulator Bit
    def test_9b_clb(self):
        mem = [0x9b]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 4,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # .byte 0x9c          ;9c         Illegal
    def test_9c_illegal(self):
        mem = [0x9c]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x9c")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # sta 0xaabb,x        ;9d bb aa   Absolute X
    def test_9d_sta(self):
        mem = [0x9d, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sta 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # .byte 0x9e          ;9e         Illegal
    def test_9e_illegal(self):
        mem = [0x9e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x9e")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # clb 4,0xaa          ;9f aa      Zero Page Bit
    def test_9f_clb(self):
        mem = [0x9f, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 4,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # ldy #0xaa           ;a0 aa      Immediate
    def test_a0_ldy(self):
        mem = [0xa0, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ldy #0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Immediate)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # lda [0xaa,x]        ;a1 aa      Indirect X
    def test_a1_lda(self):
        mem = [0xa1, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "lda [0xaa,x]")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # ldx #0xaa           ;a2 aa      Immediate
    def test_a2_ldx(self):
        mem = [0xa2, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ldx #0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Immediate)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # bbs 5,a,label30     ;a3 fe      Accumulator Bit Relative
    def test_a3_bbs(self):
        mem = [0xa3, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbs 5,a,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBitRelative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # ldy 0xaa            ;a4 aa      Zero Page
    def test_a4_ldy(self):
        mem = [0xa4, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ldy 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # lda 0xaa            ;a5 aa      Zero Page
    def test_a5_lda(self):
        mem = [0xa5, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "lda 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # ldx 0xaa            ;a6 aa      Zero Page
    def test_a6_ldx(self):
        mem = [0xa6, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ldx 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bbs 5,0xaa,label31  ;a7 aa fd   Zero Page Bit Relative
    def test_a7_bbs(self):
        mem = [0xa7, 0xaa, 0x1d]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbs 5,0xaa,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBitRelative)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # tay                 ;a8         Implied
    def test_a8_tay(self):
        mem = [0xa8]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "tay")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # lda #0xaa           ;a9 aa      Immediate
    def test_a9_lda(self):
        mem = [0xa9, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "lda #0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Immediate)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # tax                 ;aa         Implied
    def test_aa_tax(self):
        mem = [0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "tax")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # seb 5,a             ;ab         Accumulator Bit
    def test_ab_seb(self):
        mem = [0xab]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 5,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # ldy 0xaabb          ;ac bb aa   Absolute
    def test_ac_ldy(self):
        mem = [0xac, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ldy 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # lda 0xaabb          ;ad bb aa   Absolute
    def test_ad_lda(self):
        mem = [0xad, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "lda 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # ldx 0xaabb          ;ae bb aa   Absolute
    def test_ae_ldx(self):
        mem = [0xae, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ldx 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # seb 5,0xaa          ;af aa      Zero Page Bit
    def test_af_seb(self):
        mem = [0xaf, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 5,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bcs label32         ;b0 fe      Relative
    def test_b0_bcs(self):
        mem = [0xb0, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bcs 0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Relative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # lda [0xaa],y        ;b1 aa      Indirect Y
    def test_b1_lda(self):
        mem = [0xb1, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "lda [0xaa],y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectY)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # jmp [0xaa]          ;b2 aa      Zero Page Indirect
    def test_b2_jmp(self):
        mem = [0xb2, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "jmp [0xaa]")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageIndirect)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bbc 5,a,label33     ;b3 fe      Accumulator Bit Relative
    def test_b3_bbc(self):
        mem = [0xb3, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbc 5,a,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBitRelative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # ldy 0xaa,x          ;b4 aa      Zero Page X
    def test_b4_ldy(self):
        mem = [0xb4, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ldy 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # lda 0xaa,x          ;b5 aa      Zero Page X
    def test_b5_lda(self):
        mem = [0xb5, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "lda 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # ldx 0xaa,y          ;b6 aa      Zero Page Y
    def test_b6_ldx(self):
        mem = [0xb6, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ldx 0xaa,y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageY)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bbc 5,0xaa,label34  ;b7 aa fd   Zero Page Bit Relative
    def test_b7_bbc(self):
        mem = [0xb7, 0xaa, 0x1d]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbc 5,0xaa,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBitRelative)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # clv                 ;b8         Implied
    def test_b8_clv(self):
        mem = [0xb8]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clv")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # lda 0xaabb,y        ;b9 bb aa   Absolute Y
    def test_b9_lda(self):
        mem = [0xb9, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "lda 0xaabb,y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteY)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # tsx                 ;ba         Implied
    def test_ba_tsx(self):
        mem = [0xba]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "tsx")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # clb 5,a             ;bb         Accumulator Bit
    def test_bb_clb(self):
        mem = [0xbb]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 5,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # ldy 0xaabb,x        ;bc bb aa   Absolute X
    def test_bc_ldy(self):
        mem = [0xbc, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ldy 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # lda 0xaabb,x        ;bd bb aa   Absolute X
    def test_bd_lda(self):
        mem = [0xbd, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "lda 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # ldx 0xaabb,y        ;be bb aa   Absolute Y
    def test_be_ldx(self):
        mem = [0xbe, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ldx 0xaabb,y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteY)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # clb 5,0xaa          ;bf aa      Zero Page Bit
    def test_bf_clb(self):
        mem = [0xbf, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 5,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # cpy #0xaa           ;c0 aa      Immediate
    def test_c0_cpy(self):
        mem = [0xc0, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "cpy #0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Immediate)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # cmp [0xaa,x]        ;c1 aa      Indirect X
    def test_c1_cmp(self):
        mem = [0xc1, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "cmp [0xaa,x]")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # wit                 ;c2         Implied
    def test_c2_wit(self):
        mem = [0xc2]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "wit")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # bbs 6,a,label35     ;c3 fe      Accumulator Bit Relative
    def test_c3_bbs(self):
        mem = [0xc3, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbs 6,a,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBitRelative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # cpy 0xaa            ;c4 aa      Zero Page
    def test_c4_cpy(self):
        mem = [0xc4, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "cpy 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # cmp 0xaa            ;c5 aa      Zero Page
    def test_c5_cmp(self):
        mem = [0xc5, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "cmp 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # dec 0xaa            ;c6 aa      Zero Page
    def test_c6_dec(self):
        mem = [0xc6, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "dec 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bbs 6,0xaa,label36  ;c7 aa fd   Zero Page Bit Relative
    def test_c7_bbs(self):
        mem = [0xc7, 0xaa, 0x1d]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbs 6,0xaa,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBitRelative)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # iny                 ;c8         Implied
    def test_c8_iny(self):
        mem = [0xc8]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "iny")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # cmp #0xaa           ;c9 aa      Immediate
    def test_c9_cmp(self):
        mem = [0xc9, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "cmp #0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Immediate)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # dex                 ;ca         Implied
    def test_ca_dex(self):
        mem = [0xca]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "dex")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # seb 6,a             ;cb         Accumulator Bit
    def test_cb_seb(self):
        mem = [0xcb]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 6,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # cpy 0xaabb          ;cc bb aa   Absolute
    def test_cc_cpy(self):
        mem = [0xcc, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "cpy 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # cmp 0xaabb          ;cd bb aa   Absolute
    def test_cd_cmp(self):
        mem = [0xcd, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "cmp 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # dec 0xaabb          ;ce bb aa   Absolute
    def test_ce_dec(self):
        mem = [0xce, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "dec 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # seb 6,0xaa          ;cf aa      Zero Page Bit
    def test_cf_seb(self):
        mem = [0xcf, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 6,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bne label37         ;d0 fe      Relative
    def test_d0_bne(self):
        mem = [0xd0, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bne 0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Relative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # cmp [0xaa],y        ;d1 aa      Indirect Y
    def test_d1_cmp(self):
        mem = [0xd1, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "cmp [0xaa],y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectY)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # .byte 0xd2          ;d2         Illegal
    def test_d2_illegal(self):
        mem = [0xd2]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0xd2")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # bbc 6,a,label38     ;d3 fe      Accumulator Bit Relative
    def test_d3_bbc(self):
        mem = [0xd3, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbc 6,a,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBitRelative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # .byte 0xd4          ;d4         Illegal
    def test_d4_illegal(self):
        mem = [0xd4]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0xd4")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # cmp 0xaa,x          ;d5 aa      Zero Page X
    def test_d5_cmp(self):
        mem = [0xd5, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "cmp 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # dec 0xaa,x          ;d6 aa      Zero Page X
    def test_d6_cmp(self):
        mem = [0xd6, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "dec 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bbc 6,0xaa,label39  ;d7 aa fd   Zero Page Bit Relative
    def test_d7_bbc(self):
        mem = [0xd7, 0xaa, 0x1d]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbc 6,0xaa,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBitRelative)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # cld                 ;d8         Implied
    def test_d8_cld(self):
        mem = [0xd8]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "cld")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # cmp 0xaabb,y        ;d9 bb aa   Absolute Y
    def test_d9_cmp(self):
        mem = [0xd9, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "cmp 0xaabb,y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteY)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # .byte 0xda          ;da         Illegal
    def test_da_illegal(self):
        mem = [0xda]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0xda")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # clb 6,a             ;db         Accumulator Bit
    def test_db_clb(self):
        mem = [0xdb]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 6,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # .byte 0xdc          ;dc         Illegal
    def test_dc_illegal(self):
        mem = [0xdc]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0xdc")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # cmp 0xaabb,x        ;dd bb aa   Absolute X
    def test_dd_illegal(self):
        mem = [0xdd, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "cmp 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # dec 0xaabb,x        ;de bb aa   Absolute X
    def test_de_dec(self):
        mem = [0xde, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "dec 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # clb 6,0xaa          ;df aa      Zero Page Bit
    def test_df_clb(self):
        mem = [0xdf, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 6,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # cpx #0xaa           ;e0 aa      Immediate
    def test_e0_cpx(self):
        mem = [0xe0, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "cpx #0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Immediate)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # sbc [0xaa,x]        ;e1 aa      Indirect X
    def test_e1_sbc(self):
        mem = [0xe1, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sbc [0xaa,x]")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # div 0xaa,x          ;e2 aa      Zero Page X
    def test_e2_div(self):
        mem = [0xe2, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "div 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bbs 7,a,label40     ;e3 fe      Accumulator Bit Relative
    def test_e3_bbs(self):
        mem = [0xe3, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbs 7,a,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBitRelative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # cpx 0xaa            ;e4 aa      Zero Page
    def test_e4_cpx(self):
        mem = [0xe4, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "cpx 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # sbc 0xaa            ;e5 aa      Zero Page
    def test_e5_sbc(self):
        mem = [0xe5, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sbc 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # inc 0xaa            ;e6 aa      Zero Page
    def test_e6_inc(self):
        mem = [0xe6, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "inc 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bbs 7,0xaa,label41  ;e7 aa fd   Zero Page Bit Relative
    def test_e7_bbs(self):
        mem = [0xe7, 0xaa, 0x1d]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbs 7,0xaa,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBitRelative)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # inx                 ;e8         Implied
    def test_e8_inx(self):
        mem = [0xe8]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "inx")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # sbc #0xaa           ;e9 aa      Immediate
    def test_e9_sbc(self):
        mem = [0xe9, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sbc #0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Immediate)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # nop                 ;ea         Implied
    def test_ea_nop(self):
        mem = [0xea]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "nop")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # seb 7,a             ;eb         Accumulator Bit
    def test_eb_seb(self):
        mem = [0xeb]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 7,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # cpx 0xaabb          ;ec bb aa   Absolute
    def test_ec_cpx(self):
        mem = [0xec, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "cpx 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # sbc 0xaabb          ;ed bb aa   Absolute
    def test_ed_sbc(self):
        mem = [0xed, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sbc 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # inc 0xaabb          ;ee bb aa   Absolute
    def test_ee_inc(self):
        mem = [0xee, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "inc 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # seb 7,0xaa          ;ef aa      Zero Page Bit
    def test_ef_seb(self):
        mem = [0xef, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 7,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)
        self.assertEqual(inst.data_ref_address, 0xaa)
        self.assertEqual(inst.code_ref_address, None)

    # beq label42         ;f0 fe      Relative
    def test_f0_beq(self):
        mem = [0xf0, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "beq 0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Relative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # sbc [0xaa],y        ;f1 aa      Indirect Y
    def test_f1_sbc(self):
        mem = [0xf1, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sbc [0xaa],y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectY)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # .byte 0xf2          ;f2         Illegal
    def test_f2_illegal(self):
        mem = [0xf2]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0xf2")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # bbc 7,a,label43     ;f3 fe      Accumulator Bit Relative
    def test_f3_bbc(self):
        mem = [0xf3, 0x1e]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbc 7,a,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBitRelative)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # .byte 0xf4          ;f4         Illegal
    def test_f4_illegal(self):
        mem = [0xf4]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0xf4")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # sbc 0xaa,x          ;f5 aa      Zero Page X
    def test_f5_sbc(self):
        mem = [0xf5, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sbc 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # inc 0xaa,x          ;f6 aa      Zero Page X
    def test_f6_inc(self):
        mem = [0xf6, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "inc 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)

    # bbc 7,0xaa,label44  ;f7 aa fd   Zero Page Bit Relative
    def test_f7_bbc(self):
        mem = [0xf7, 0xaa, 0x1d]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bbc 7,0xaa,0x0020")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBitRelative)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, 0x0020)

    # sed                 ;f8         Implied
    def test_f8_sed(self):
        mem = [0xf8]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sed")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # sbc 0xaabb,y        ;f9 bb aa   Absolute Y
    def test_f9_sbc(self):
        mem = [0xf9, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sbc 0xaabb,y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteY)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # .byte 0xfa          ;fa         Illegal
    def test_fa_illegal(self):
        mem = [0xfa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0xfa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # clb 7,a             ;fb         Accumulator Bit
    def test_fb_clb(self):
        mem = [0xfb]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 7,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # .byte 0xfc          ;fc         Illegal
    def test_fc_illegal(self):
        mem = [0xfc]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0xfc")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)
        self.assertEqual(inst.data_ref_address, None)
        self.assertEqual(inst.code_ref_address, None)

    # sbc 0xaabb,x        ;fd bb aa   Absolute X
    def test_fd_sbc(self):
        mem = [0xfd, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sbc 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # inc 0xaabb,x        ;fe bb aa   Absolute X
    def test_fe_inc(self):
        mem = [0xfe, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "inc 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)
        self.assertEqual(inst.data_ref_address, 0xaabb)
        self.assertEqual(inst.code_ref_address, None)

    # clb 7,0xaa          ;ff aa      Zero Page Bit
    def test_ff_clb(self):
        mem = [0xff, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 7,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)
        self.assertEqual(inst.data_ref_address, 0x00aa)
        self.assertEqual(inst.code_ref_address, None)


def test_suite():
    return unittest.findTestCases(sys.modules[__name__])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
