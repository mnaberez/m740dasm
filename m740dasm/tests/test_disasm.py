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

    # ora [0xaa,x]        ;01 aa      Indirect X
    def test_01_ora(self):
        mem = [0x01, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ora [0xaa,x]")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectX)

    # jsr [0xaa]          ;02 aa      Zero Page Indirect
    def test_01_jsr(self):
        mem = [0x02, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "jsr [0xaa]")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageIndirect)

    # bbs 0,a,label4      ;03 fe      Accumulator Bit Relative
    def test_03_bbs(self):
        pass # TODO rel

    # .byte 0x04          ;04         Illegal
    def test_04_illegal(self):
        mem = [0x04]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x04")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)

    # ora 0xaa            ;05 aa      Zero Page
    def test_05_ora(self):
        mem = [0x05, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ora 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)

    # asl 0x45            ;06 45      Zero Page
    def test_06_asl(self):
        mem = [0x06, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "asl 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)

    # bbs 0,0xaa,label5   ;07 aa fd   Zero Page Bit Relative
    def test_07_bbs(self):
        pass # TODO rel

    # php                 ;08         Implied
    def test_08_php(self):
        mem = [0x08]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "php")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)

    # ora #0xaa           ;09 aa      Immediate
    def test_09_ora(self):
        mem = [0x09, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ora #0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Immediate)

    # asl a               ;0a         Implied
    def test_0a_asl(self):
        mem = [0x0a]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "asl a")
        self.assertEqual(len(inst), len(mem))

    # seb 0,a             ;0b         Accumulator Bit
    def test_0b_seb(self):
        mem = [0x0b]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 0,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)

    # .byte 0x0c          ;0c         Illegal
    def test_0c_illegal(self):
        mem = [0x0c]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x0c")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)

    # ora 0xaabb          ;0d bb aa   Absolute
    def test_0d_ora(self):
        mem = [0x0d, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ora 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)

    # asl 0xaabb          ;0e bb aa   Absolute
    def test_0e_abs(self):
        mem = [0x0e, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "asl 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)

    # seb 0,0xaa          ;0f aa      Zero Page Bit
    def test_0f_seb(self):
        mem = [0x0f, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 0,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)

    # bpl label6          ;10 fe      Relative
    def test_10_bpl(self):
        # TODO rel
        pass

    # ora [0xaa],y        ;11 aa      Indirect Y
    def test_11_ora(self):
        mem = [0x11, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ora [0xaa],y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectY)

    # clt                 ;12         Implied
    def test_12_clt(self):
        mem = [0x12]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clt")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)

    # bbc 0,a,label7      ;13 fe      Accumulator Bit Relative
    def test_13_bbc(self):
        pass # TODO rel

    # .byte 0x14          ;14         Illegal
    def test_14_illegal(self):
        mem = [0x14]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x14")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)

    # ora 0xaa,x          ;15 aa      Zero Page X
    def test_15_ora(self):
        mem = [0x15, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ora 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)

    # asl 0xaa,x          ;16 aa      Zero Page X
    def test_16_asl(self):
        mem = [0x16, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "asl 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)

    # bbc 0,0xaa,label8   ;17 aa fd   Zero Page Bit Relative
    def test_17_bbc(self):
        pass # TODO rel

    # clc                 ;18         Implied
    def test_18_clc(self):
        mem = [0x18]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clc")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)

    # ora 0xaabb,y        ;19 bb aa   Absolute Y
    def test_19_ora(self):
        mem = [0x19, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ora 0xaabb,y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteY)

    # dec a               ;1a         Implied
    def test_1a_dec(self):
        mem = [0x1a]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "dec a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)

    # clb 0,a             ;1b         Accumulator Bit
    def test_1b_clb(self):
        mem = [0x1b]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 0,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)

    # .byte 0x1c          ;1c         Illegal
    def test_1c_illegal(self):
        mem = [0x1c]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x1c")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)

    # ora 0xaabb,x        ;1d bb aa   Absolute X
    def test_1d_ora(self):
        mem = [0x1d, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ora 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)

    # asl 0xaabb,x        ;1e bb aa   Absolute X
    def test_1e_asl(self):
        mem = [0x1e, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "asl 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)

    # clb 0,0xaa          ;1f aa      Zero Page Bit
    def test_1f_clb(self):
        mem = [0x1f, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 0,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)

    # jsr 0xaabb          ;20 bb aa   Absolute
    def test_20_jsr(self):
        mem = [0x20, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "jsr 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)

    # and [0xaa,x]        ;21 aa      Indirect X
    def test_21_and(self):
        mem = [0x21, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "and [0xaa,x]")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectX)

    # jsr \0xffaa         ;22         Special Page
    def test_22_jsr(self):
        mem = [0x22, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "jsr \\0xffaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.SpecialPage)

    # bbs 1,a,label9      ;23 fe      Zero Page Bit Relative
    def test_23_bbs(self):
        pass # TODO rel

    # bit 0xaa            ;24 aa      Zero Page
    def test_24_bit(self):
        mem = [0x24, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bit 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)

    # and 0xaa            ;25 aa      Zero Page
    def test_25_and(self):
        mem = [0x25, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "and 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)

    # rol 0xaa            ;26 aa      Zero Page
    def test_26_rol(self):
        mem = [0x26, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "rol 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)

    # bbs 1,0xaa,label10  ;27 aa fd   Zero Page Bit Relative
    def test_27_bbs(self):
        mem = [0x27, 0xaa, 0xfd]
        # TODO relative

    # plp                 ;28         Implied
    def test_28_plp(self):
        mem = [0x28]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "plp")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)

    # and #0xaa           ;29 aa      Immediate
    def test_29_plp(self):
        mem = [0x29, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "and #0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Immediate)

    # bmi label11         ;30 fe      Relative
    def test_29_plp(self):
        pass # TODO relative

    # rol a               ;2a         Implied
    def test_2a_rol(self):
        mem = [0x2a]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "rol a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)

    # seb 1,a             ;2b         Accumulator Bit
    def test_2b_seb(self):
        mem = [0x2b]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 1,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)

    # bit 0xaabb          ;2c bb aa   Absolute
    def test_2c_bit(self):
        mem = [0x2c, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "bit 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)

    # and 0xaabb          ;2d bb aa   Absolute
    def test_2d_and(self):
        mem = [0x2d, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "and 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)

    # rol 0xaabb          ;2e bb aa   Absolute
    def test_2e_rol(self):
        mem = [0x2e, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "rol 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)

    # seb 1,0xaa          ;2f aa      Zero Page Bit
    def test_2f_seb(self):
        mem = [0x2f, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 1,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)

    # bmi label11         ;30 fe      Relative
    def test_30_bmi(self):
        pass # TODO relative

    # and [0xaa],y        ;31 aa      Indirect Y
    def test_31_and(self):
        mem = [0x31, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "and [0xaa],y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectY)

    # set                 ;32         Implied
    def test_32_set(self):
        mem = [0x32]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "set")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)

    # bbc 1,a,label12     ;33 fe      Accumulator Bit Relative
    def test_33_bbc(self):
        pass # TODO relative

    # .byte 0x34          ;34 00      Illegal
    def test_34_illegal(self):
        mem = [0x34]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x34")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)

    # and 0xaa,x          ;35 aa      Zero Page X
    def test_35_and(self):
        mem = [0x35, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "and 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)

    # rol 0xaa,x          ;36 aa      Zero Page X
    def test_36_rol(self):
        mem = [0x36, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "rol 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)

    # bbc 1,0xaa,label13  ;37 aa fd   Zero Page Bit Relative
    def test_37_bbc(self):
        pass # TODO relative

    # sec                 ;38         Implied
    def test_38_sec(self):
        mem = [0x38]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sec")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)

    # and 0xaabb,y        ;39 bb aa   Absolute Y
    def test_39_and(self):
        mem = [0x39, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "and 0xaabb,y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteY)

    # inc a               ;3a         Implied
    def test_3a_inc(self):
        mem = [0x3a]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "inc a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)

    # ldm #0xaa,0xbb      ;3c aa bb   Zero Page Immediate
    def test_3c_ldm(self):
        mem = [0x3c, 0xaa, 0xbb]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ldm #0xaa,0xbb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageImmediate)

    # and 0xaabb,x        ;3d bb aa   Absolute X
    def test_3d_and(self):
        mem = [0x3d, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "and 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)

    # rol 0xaabb,x        ;3e bb aa   Absolute X
    def test_3e_rol(self):
        mem = [0x3e, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "rol 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)

    # clb 1,0xaa          ;3f aa      Zero Page Bit
    def test_3f_clb(self):
        mem = [0x3f, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 1,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)

    # rti                 ;40         Implied
    def test_40_rti(self):
        mem = [0x40]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "rti")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)

    # eor [0xaa,x]        ;41 aa      Indirect X
    def test_41_eor(self):
        mem = [0x41, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "eor [0xaa,x]")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectX)

    # stp                 ;42         Implied
    def test_42_stp(self):
        mem = [0x42]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "stp")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)

    # bbs 2,a,label14     ;43 fe      Accumulator Bit
    def test_43_bbs(self):
        pass # TODO relative

    # com 0xaa            ;44 aa      Zero Page
    def test_44_com(self):
        mem = [0x44, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "com 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)

    # eor 0xaa            ;45 aa      Zero Page
    def test_45_eor(self):
        mem = [0x45, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "eor 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)

    # lsr 0xaa            ;46 aa      Zero Page
    def test_46_lsr(self):
        mem = [0x46, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "lsr 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)

    # bbs 2,0xaa,label15  ;47 aa fd   Zero Page Bit Relative
    def test_47_bbs(self):
        pass # TODO relative

    # pha                 ;48         Implied
    def test_48_pha(self):
        mem = [0x48]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "pha")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)

    # eor #0xaa           ;49 aa      Immediate
    def test_49_eor(self):
        mem = [0x49, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "eor #0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Immediate)

    # lsr a               ;4a         Implied
    def test_4a_lsr(self):
        mem = [0x4a]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "lsr a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)

    # seb 2,a             ;4b         Accumulator Bit
    def test_4b_seb(self):
        mem = [0x4b]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 2,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)

    # jmp 0xaabb          ;4c bb aa   Absolute
    def test_4c_jmp(self):
        mem = [0x4c, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "jmp 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)

    # eor 0xaabb          ;4d bb aa   Absolute
    def test_4d_eor(self):
        mem = [0x4d, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "eor 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)

    # lsr 0xaabb          ;4e bb aa   Absolute
    def test_4e_lsr(self):
        mem = [0x4e, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "lsr 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)

    # seb 2,0xaa          ;4f aa      Zero Page Bit
    def test_4f_seb(self):
        mem = [0x4f, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 2,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)

    # bvc label16         ;50 fe      Relative
    def test_50_bvc(self):
        pass # TODO relative

    # eor [0xaa],y        ;51 aa      Indirect Y
    def test_51_eor(self):
        mem = [0x51, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "eor [0xaa],y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectY)

    # .byte 0x52          ;52         Illegal
    def test_52_illegal(self):
        mem = [0x52]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x52")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)

    # bbc 2,a,label17     ;53 fe      Accumulator Bit Relative
    def test_53_bbc(self):
        pass # TODO relative

    # .byte 0x54          ;54         Illegal
    def test_54_illegal(self):
        mem = [0x54]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x54")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)

    # eor 0xaa,x          ;55 aa      Zero Page X
    def test_55_eor(self):
        mem = [0x55, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "eor 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)

    # lsr 0xaa,x          ;56 aa      Zero Page X
    def test_56_lsr(self):
        mem = [0x56, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "lsr 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)

    # bbc 2,0xaa,label18  ;57 aa fd   Zero Page Bit Relative
    def test_57_bbc(self):
        pass # TODO relative

    # cli                 ;58         Implied
    def test_58_cli(self):
        mem = [0x58]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "cli")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)

    # eor 0xaabb,y        ;59 bb aa   Absolute Y
    def test_59_eor(self):
        mem = [0x59, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "eor 0xaabb,y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteY)

    # .byte 0x5a          ;5a         Illegal
    def test_5a_illegal(self):
        mem = [0x5a]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x5a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)

    # clb 2,a             ;5b         Accumulator Bit
    def test_5b_clb(self):
        mem = [0x5b]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 2,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)

    # .byte 0x5c          ;5c         Illegal
    def test_5c_illegal(self):
        mem = [0x5c]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x5c")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)

    # eor 0xaabb,x        ;5d bb aa   Absolute X
    def test_5d_eor(self):
        mem = [0x5d, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "eor 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)

    # lsr 0xaabb,x        ;5e bb aa   Absolute X
    def test_5e_lsr(self):
        mem = [0x5e, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "lsr 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)

    # clb 2,0xaa          ;5f aa      Zero Page Bit
    def test_5f_clb(self):
        mem = [0x5f, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 2,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)

    # rts                 ;60         Implied
    def test_60_rts(self):
        mem = [0x60]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "rts")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)

    # adc [0xaa,x]        ;61 aa      Indirect X
    def test_61_adc(self):
        mem = [0x61, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "adc [0xaa,x]")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectX)

    # mul 0xaa,x          ;62 aa      Zero Page X
    def test_62_mul(self):
        mem = [0x62, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "mul 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)

    # bbs 3,a,label19     ;63 fe      Accumulator Bit Relative
    def test_63_bbs(self):
        pass # TODO relative

    # tst 0xaa            ;64 aa      Zero Page
    def test_64_tst(self):
        mem = [0x64, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "tst 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)

    # adc 0xaa            ;65 aa      Zero Page
    def test_65_adc(self):
        mem = [0x65, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "adc 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)

    # ror 0xaa            ;66 aa      Zero Page
    def test_66_ror(self):
        mem = [0x66, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ror 0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPage)

    # bbs 3,0xaa,label20  ;67 aa fd   Zero Page Bit Relative
    def test_67_bbs(self):
        pass # TODO relative

    # pla                 ;68         Implied
    def test_68_pla(self):
        mem = [0x68]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "pla")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)

    # adc #0xaa           ;69 aa      Immediate
    def test_69_adc(self):
        mem = [0x69, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "adc #0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Immediate)

    # ror a               ;6a         Implied
    def test_6a_ror(self):
        mem = [0x6a]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ror a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)

    # seb 3,a             ;6b         Accumulator Bit
    def test_6b_seb(self):
        mem = [0x6b]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 3,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)

    # jmp [0xaabb]        ;6c bb aa   Indirect Absolute
    def test_6c_jmp(self):
        mem = [0x6c, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "jmp [0xaabb]")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectAbsolute)

    # adc 0xaabb          ;6d bb aa   Absolute
    def test_6d_adc(self):
        mem = [0x6d, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "adc 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)

    # ror 0xaabb          ;6e bb aa   Absolute
    def test_6e_ror(self):
        mem = [0x6e, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ror 0xaabb")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Absolute)

    # seb 3,0xaa          ;6f aa      Zero Page Bit
    def test_6f_seb(self):
        mem = [0x6f, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "seb 3,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)

    # bvs label21         ;70 fe      Relative
    def test_70_bvs(self):
        pass # TODO relative

    # adc [0xaa],y        ;71 aa      Indirect Y
    def test_71_adc(self):
        mem = [0x71, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "adc [0xaa],y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.IndirectY)

    # .byte 0x72          ;72         Illegal
    def test_72_illegal(self):
        mem = [0x72]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x72")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)

    # bbc 3,a,label22     ;73 fe      Accumulator Bit Relative
    def test_73_bbc(self):
        pass # TODO relative

    # .byte 0x74          ;74         Illegal
    def test_74_illegal(self):
        mem = [0x74]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x74")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)

    # adc 0xaa,x          ;75 aa      Zero Page X
    def test_75_adc(self):
        mem = [0x75, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "adc 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)

    # ror 0xaa,x          ;76 aa      Zero Page X
    def test_76_ror(self):
        mem = [0x76, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ror 0xaa,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageX)

    # bbc 3,0xaa,label23  ;77 aa fd   Zero Page Bit Relative
    def test_77_bbc(self):
        pass # TODO relative

    # sei                 ;78         Implied
    def test_78_sei(self):
        mem = [0x78]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "sei")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Implied)

    # adc 0xaabb,y        ;79 bb aa   Absolute Y
    def test_79_adc(self):
        mem = [0x79, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "adc 0xaabb,y")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteY)

    # .byte 0x7a          ;7a         Illegal
    def test_7a_illegal(self):
        mem = [0x7a]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x7a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)

    # clb 3,a             ;7b         Accumulator Bit
    def test_7b_clb(self):
        mem = [0x7b]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 3,a")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AccumulatorBit)

    # .byte 0x7a          ;7c         Illegal
    def test_7c_illegal(self):
        mem = [0x7c]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), ".byte 0x7c")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.Illegal)

    # adc 0xaabb,x        ;7d bb aa   Absolute X
    def test_7d_adc(self):
        mem = [0x7d, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "adc 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)

    # ror 0xaabb,x        ;7e bb aa   Absolute X
    def test_7e_ror(self):
        mem = [0x7e, 0xbb, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "ror 0xaabb,x")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.AbsoluteX)

    # clb 3,0xaa          ;7f aa      Zero Page Bit
    def test_7f_clb(self):
        mem = [0x7f, 0xaa]
        inst = disassemble_inst(mem, pc=0)
        self.assertEqual(str(inst), "clb 3,0xaa")
        self.assertEqual(len(inst), len(mem))
        self.assertEqual(inst.addr_mode, AddressModes.ZeroPageBit)


def test_suite():
    return unittest.findTestCases(sys.modules[__name__])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
