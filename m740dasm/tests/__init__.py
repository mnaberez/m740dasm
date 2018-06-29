import sys
import unittest

from m740dasm.disassemble import disassemble


class disassemble_tests(unittest.TestCase):
    def test_00_brk(self):
        mem = [0x00]
        inst = disassemble(mem, pc=0)
        self.assertEqual(str(inst), "brk")
        self.assertEqual(len(inst), len(mem))


def test_suite():
    return unittest.findTestCases(sys.modules[__name__])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
