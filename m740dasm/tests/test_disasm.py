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


def test_suite():
    return unittest.findTestCases(sys.modules[__name__])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
