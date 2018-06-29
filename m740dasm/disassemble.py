class AddressModes(object):
    Illegal                 = 0     # .byte 0x04      04
    Immediate               = 1     # ADC #$A5        69 A5
    Accumulator             = 2     # ROL A           2A
    ZeroPage                = 3     # ADC $40         65 40
    ZeroPageX               = 4     # ADC $5E,X       75 5E
    ZeroPageY               = 5     # LDX $62,Y       B6 62
    Absolute                = 6     # ADC $AD12       6D 12 AD
    AbsoluteX               = 7     # ADC $AD12,X     7D 12 AD
    AbsoluteY               = 8     # ADC $AD12,Y     79 12 AD
    Implied                 = 9     # CLC             18
    Relative                = 10    # BCC *-12        90 F2
    IndirectX               = 11    # ADC ($1E,X)     61 1E
    IndirectY               = 12    # ADC ($1E),Y     71 1E
    IndirectAbsolute        = 13    # JMP ($1400)     6C 00 14
    ZeroPageIndirect        = 14    # JMP ($45)       B2 45
    SpecialPage             = 15    # JMP \$FFC0      22 C0
    ZeroPageBit             = 16    # CLB 5,$44       BF 44
    AccumulatorBit          = 17    # CLB 5,A         BB
    AccumulatorBitRelative  = 18    # BC 5,A,*-12     B3 F2
    ZeroPageBitRelative     = 19    # BBC 5,$04,*-12  B7 04 F1
    ZeroPageImmediate       = 20    # LDM #0xaa,0xbb  3C AA BB

InstructionLengths = {
    AddressModes.Illegal:                 1,
    AddressModes.Immediate:               1,
    AddressModes.Accumulator:             1,
    AddressModes.ZeroPage:                2,
    AddressModes.ZeroPageX:               2,
    AddressModes.ZeroPageY:               2,
    AddressModes.Absolute:                3,
    AddressModes.AbsoluteX:               3,
    AddressModes.AbsoluteY:               3,
    AddressModes.Implied:                 1,
    AddressModes.Relative:                2,
    AddressModes.IndirectX:               2,
    AddressModes.IndirectY:               2,
    AddressModes.IndirectAbsolute:        3,
    AddressModes.ZeroPageIndirect:        2,
    AddressModes.SpecialPage:             2,
    AddressModes.ZeroPageBit:             2,
    AddressModes.AccumulatorBit:          2,
    AddressModes.AccumulatorBitRelative:  3,
    AddressModes.ZeroPageBitRelative:     3,
    AddressModes.ZeroPageImmediate:       3,
}

class Instruction(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

Instructions = (
    # brk                 ;00         Implied
    Instruction(opcode=0x00,
                template="brk",
                addr_mode=AddressModes.Implied,
                ),
    # ora [0x1E,x]        ;01 1e      Indirect X
    Instruction(opcode=0x01,
                template="ora [0x1E,x]",
                addr_mode=AddressModes.IndirectX,
                ),
    # jsr [0x45]          ;02 45      Zero Page Indirect
    Instruction(opcode=0x02,
                template="jsr [0x45]",
                addr_mode=AddressModes.ZeroPageIndirect,
                ),
    # bbs 0,a,label4      ;03 fe      Accumulator Bit Relative
    Instruction(opcode=0x03,
                template="bbs 0,a,label4",
                addr_mode=AddressModes.AccumulatorBitRelative,
                ),
    # .byte 0x04          ;04 00      Illegal
    Instruction(opcode=0x04,
                template=".byte 0x04",
                addr_mode=AddressModes.Illegal,
                ),
    # ora 0x45            ;05 45      Zero Page
    Instruction(opcode=0x05,
                template="ora 0x45",
                addr_mode=AddressModes.ZeroPage,
                ),
    # asl 0x45            ;06 45      Zero Page
    Instruction(opcode=0x06,
                template="asl 0x45",
                addr_mode=AddressModes.ZeroPage,
                ),
    # bbs 0,0xaa,label5   ;07 aa fd   Zero Page Bit Relative
    Instruction(opcode=0x07,
                template="bbs 0,0xaa,label5",
                addr_mode=AddressModes.ZeroPageBitRelative,
                ),
    # php                 ;08         Implied
    Instruction(opcode=0x08,
                template="php",
                addr_mode=AddressModes.Implied,
                ),
    # ora #0xaa           ;09 aa      Immediate
    Instruction(opcode=0x09,
                template="ora #0xaa",
                addr_mode=AddressModes.Immediate,
                ),
    # asl a               ;0a         Implied
    Instruction(opcode=0x0a,
                template="asl a",
                addr_mode=AddressModes.Implied,
                ),
    # seb 0,a             ;0b         Accumulator Bit Relative
    Instruction(opcode=0x0b,
                template="seb 0,a",
                addr_mode=AddressModes.AccumulatorBitRelative,
                ),
    # .byte 0x0c          ;0c         Illegal
    Instruction(opcode=0x0c,
                template=".byte 0x0c",
                addr_mode=AddressModes.Illegal,
                ),
    # ora 0xaabb          ;0d bb aa   Absolute
    Instruction(opcode=0x0d,
                template="ora 0xaabb",
                addr_mode=AddressModes.Absolute,
                ),
    # asl 0xaabb          ;0e bb aa   Absolute
    Instruction(opcode=0x0e,
                template="asl 0xaabb",
                addr_mode=AddressModes.Absolute,
                ),
    # seb 0,0xaa          ;0f aa      Zero Page Bit
    Instruction(opcode=0x0f,
                template="seb 0,0xaa",
                addr_mode=AddressModes.ZeroPageBit,
                ),
    # bpl label6          ;10 fe      Relative
    Instruction(opcode=0x10,
                template="bpl label6",
                addr_mode=AddressModes.Relative,
                ),
    # ora [0xaa],y        ;11 aa      Indirect Y
    Instruction(opcode=0x11,
                template="ora [0xaa],y",
                addr_mode=AddressModes.IndirectY,
                ),
    # clt                 ;12         Implied
    Instruction(opcode=0x12,
                template="clt",
                addr_mode=AddressModes.Implied,
                ),
    # bbc 0,a,label7      ;13 fe      Accumulator Bit Relative
    Instruction(opcode=0x13,
                template="bbc 0,a,label7",
                addr_mode=AddressModes.AccumulatorBitRelative,
                ),
    # .byte 0x14          ;14         Illegal
    Instruction(opcode=0x14,
                template=".byte 0x14",
                addr_mode=AddressModes.Illegal,
                ),
    # ora 0xaa,x          ;15 aa      Zero Page X
    Instruction(opcode=0x15,
                template="ora 0xaa,x",
                addr_mode=AddressModes.ZeroPageX,
                ),
    # asl 0xaa,x          ;16 aa      Zero Page X
    Instruction(opcode=0x16,
                template="asl 0xaa,x",
                addr_mode=AddressModes.ZeroPageX,
                ),
    # bbc 0,0xaa,label8   ;17 aa fd   Zero Page Bit Relative
    Instruction(opcode=0x17,
                template="bbc 0,0xaa,label8",
                addr_mode=AddressModes.ZeroPageX,
                ),
    # clc                 ;18         Implied
    Instruction(opcode=0x18,
                template="clc",
                addr_mode=AddressModes.Implied,
                ),
    # ora 0xaabb,y        ;19 bb aa   Absolute Y
    Instruction(opcode=0x19,
                template="ora 0xaabb,y",
                addr_mode=AddressModes.Implied,
                ),
    # dec a               ;1a         Implied
    Instruction(opcode=0x1a,
                template="dec a",
                addr_mode=AddressModes.Implied,
                ),
    # clb 0,a             ;1b         Accumulator Bit
    Instruction(opcode=0x1b,
                template="clb 0,a",
                addr_mode=AddressModes.AccumulatorBit,
                ),
    # .byte 0x1c          ;1c         Illegal
    Instruction(opcode=0x1c,
                template=".byte 0x1c",
                addr_mode=AddressModes.Illegal,
                ),
    # ora 0xaabb,x        ;1d bb aa   Absolute X
    Instruction(opcode=0x1d,
                template="ora 0xaabb,x",
                addr_mode=AddressModes.AbsoluteX,
                ),
    # asl 0xaabb,x        ;1e bb aa   Absolute X
    Instruction(opcode=0x1e,
                template="asl 0xaabb,x",
                addr_mode=AddressModes.AbsoluteX,
                ),
    # clb 0,0xaa          ;1f aa      Zero Page Bit
    Instruction(opcode=0x1f,
                template="clb 0,0xaa",
                addr_mode=AddressModes.ZeroPageBit,
                ),
    # jsr 0xaabb          ;20 bb aa   Absolute
    Instruction(opcode=0x20,
                template="jsr 0xaabb",
                addr_mode=AddressModes.Absolute,
                ),
    # and [0xaa,x]        ;21 aa      Indirect X
    Instruction(opcode=0x21,
                template="and [0xaa,x]",
                addr_mode=AddressModes.IndirectX,
                ),
    # jsr \0xffaa         ;22         Special Page
    Instruction(opcode=0x22,
                template="jsr \\0xffaa",
                addr_mode=AddressModes.IndirectX,
                ),
    # bbs 1,a,label9      ;23 fe      Zero Page Bit Relative
    Instruction(opcode=0x23,
                template="bbs 1,a,label9",
                addr_mode=AddressModes.ZeroPageBitRelative,
                ),
    # bit 0xaa            ;24 aa      Zero Page
    Instruction(opcode=0x24,
                template="bit 0xaa",
                addr_mode=AddressModes.ZeroPage,
                ),
    # and 0xaa            ;25 aa      Zero Page
    Instruction(opcode=0x25,
                template="and 0xaa",
                addr_mode=AddressModes.ZeroPage,
                ),
    # rol 0xaa            ;26 aa      Zero Page
    Instruction(opcode=0x26,
                template="rol 0xaa",
                addr_mode=AddressModes.ZeroPage,
                ),
    # bbs 1,0xaa,label10  ;27 aa fd   Zero Page Bit Relative
    Instruction(opcode=0x27,
                template="bbs 1,0xaa,label10",
                addr_mode=AddressModes.ZeroPage,
                ),
    # plp                 ;28         Implied
    Instruction(opcode=0x28,
                template="plp",
                addr_mode=AddressModes.Implied,
                ),
    # and #0xaa           ;29         Immediate
    Instruction(opcode=0x29,
                template="and #0xaa",
                addr_mode=AddressModes.Immediate,
                ),
    # rol a               ;2a         Implied
    Instruction(opcode=0x2a,
                template="rol a",
                addr_mode=AddressModes.Implied,
                ),
    # seb 1,a             ;2b         Accumulator Bit
    Instruction(opcode=0x2b,
                template="seb 1,a",
                addr_mode=AddressModes.AccumulatorBit,
                ),
    # bit 0xaabb          ;2c bb aa   Absolute
    Instruction(opcode=0x2c,
                template="bit 0xaabb",
                addr_mode=AddressModes.Absolute,
                ),
    # and 0xaabb          ;2d bb aa   Absolute
    Instruction(opcode=0x2d,
                template="and 0xaabb",
                addr_mode=AddressModes.Absolute,
                ),
    # rol 0xaabb          ;2e bb aa   Absolute
    Instruction(opcode=0x2e,
                template="rol 0xaabb",
                addr_mode=AddressModes.Absolute,
                ),
    # seb 1,0xaa          ;2f aa      Zero Page Bit
    Instruction(opcode=0x2f,
                template="seb 1,0xaa",
                addr_mode=AddressModes.ZeroPageBit,
                ),
    # bmi label11         ;30 fe      Relative
    Instruction(opcode=0x30,
                template="bmi label11",
                addr_mode=AddressModes.Relative,
                ),
    # and [0xaa],y        ;31 aa      Indirect Y
    Instruction(opcode=0x31,
                template="and [0xaa],y",
                addr_mode=AddressModes.IndirectY,
                ),
    # set                 ;32         Implied
    Instruction(opcode=0x32,
                template="set",
                addr_mode=AddressModes.Implied,
                ),
    # bbc 1,a,label12     ;33 fe      Accumulator Bit Relative
    Instruction(opcode=0x33,
                template="bbc 1,a,label12",
                addr_mode=AddressModes.AccumulatorBitRelative,
                ),
    # .byte 0x34          ;34 00      Illegal
    Instruction(opcode=0x34,
                template=".byte 0x34",
                addr_mode=AddressModes.Illegal,
                ),
    # and 0xaa,x          ;35 aa      Zero Page X
    Instruction(opcode=0x35,
                template="and 0xaa,x",
                addr_mode=AddressModes.ZeroPageX,
                ),
    # rol 0xaa,x          ;36 aa      Zero Page X
    Instruction(opcode=0x36,
                template="rol 0xaa,x",
                addr_mode=AddressModes.ZeroPageX,
                ),
    # bbc 1,0xaa,label13  ;37 aa fd   Zero Page Bit Relative
    Instruction(opcode=0x37,
                template="bbc 1,0xaa,label13",
                addr_mode=AddressModes.ZeroPageBitRelative,
                ),
    # sec                 ;38         Implied
    Instruction(opcode=0x38,
                template="sec",
                addr_mode=AddressModes.Implied,
                ),
    # and 0xaabb,y        ;39 bb aa   Absolute Y
    Instruction(opcode=0x39,
                template="and 0xaabb,y",
                addr_mode=AddressModes.AbsoluteY,
                ),
    # inc a               ;3a         Implied
    Instruction(opcode=0x3a,
                template="inc a",
                addr_mode=AddressModes.Implied,
                ),
    # clb 1,a             ;3b         Accumulator Bit
    Instruction(opcode=0x3b,
                template="clb 1,a",
                addr_mode=AddressModes.AccumulatorBit,
                ),
    # ldm #0xaa,0xbb      ;3c aa bb   Zero Page Immediate
    Instruction(opcode=0x3c,
                template="ldm #0xaa,0xbb",
                addr_mode=AddressModes.ZeroPageImmediate,
                ),
    # and 0xaabb,x        ;3d bb aa   Absolute X
    Instruction(opcode=0x3d,
                template="and 0xaabb,x",
                addr_mode=AddressModes.AbsoluteX,
                ),
    # rol 0xaabb,x        ;3e bb aa   Absolute X
    Instruction(opcode=0x3e,
                template="rol 0xaabb,x",
                addr_mode=AddressModes.AbsoluteX,
                ),
    # clb 1,0xaa          ;3f aa      Zero Page Bit
    Instruction(opcode=0x3f,
                template="clb 1,0xaa",
                addr_mode=AddressModes.ZeroPageBit,
                ),
    # rti                 ;40         Implied
    Instruction(opcode=0x40,
                template="rti",
                addr_mode=AddressModes.Implied,
                ),
    # eor [0xaa,x]        ;41 aa      Indirect X
    Instruction(opcode=0x41,
                template="eor [0xaa,x]",
                addr_mode=AddressModes.IndirectX,
                ),
    # stp                 ;42         Implied
    Instruction(opcode=0x42,
                template="stp",
                addr_mode=AddressModes.Implied,
                ),
    # bbs 2,a,label14     ;43 fe      Accumulator Bit
    Instruction(opcode=0x43,
                template="bbs 2,a,label14",
                addr_mode=AddressModes.AccumulatorBit,
                ),
    # com 0xaa            ;44 aa      Zero Page
    Instruction(opcode=0x44,
                template="com 0xaa",
                addr_mode=AddressModes.ZeroPage,
                ),
    # eor 0xaa            ;45 aa      Zero Page
    Instruction(opcode=0x45,
                template="eor 0xaa",
                addr_mode=AddressModes.ZeroPage,
                ),
    # lsr 0xaa            ;46 aa      Zero Page
    Instruction(opcode=0x46,
                template="lsr 0xaa",
                addr_mode=AddressModes.ZeroPage,
                ),
    # bbs 2,0xaa,label15  ;47 aa fd   Zero Page Bit Relative
    Instruction(opcode=0x47,
                template="bbs 2,0xaa,label15",
                addr_mode=AddressModes.ZeroPageBitRelative,
                ),
    # pha                 ;48         Implied
    Instruction(opcode=0x48,
                template="pha",
                addr_mode=AddressModes.Implied,
                ),
    # eor #0xaa           ;49 aa      Immediate
    Instruction(opcode=0x49,
                template="eor #0xaa",
                addr_mode=AddressModes.Immediate,
                ),
    # lsr a               ;4a         Implied
    Instruction(opcode=0x4a,
                template="lsr a",
                addr_mode=AddressModes.Implied,
                ),
    # seb 2,a             ;4b         Accumulator Bit
    Instruction(opcode=0x4b,
                template="seb 2,a",
                addr_mode=AddressModes.AccumulatorBit,
                ),
    # jmp 0xaabb          ;4c bb aa   Absolute
    Instruction(opcode=0x4c,
                template="jmp 0xaabb",
                addr_mode=AddressModes.Absolute,
                ),
    # eor 0xaabb          ;4d bb aa   Absolute
    Instruction(opcode=0x4d,
                template="eor 0xaabb",
                addr_mode=AddressModes.Absolute,
                ),
    # lsr 0xaabb          ;4e bb aa   Absolute
    Instruction(opcode=0x4e,
                template="lsr 0xaabb",
                addr_mode=AddressModes.Absolute,
                ),
    # seb 2,0xaa          ;4f aa      Zero Page Bit
    Instruction(opcode=0x4f,
                template="seb 2,0xaa",
                addr_mode=AddressModes.ZeroPageBit,
                ),
    # bvc label16         ;50 fe      Relative
    Instruction(opcode=0x50,
                template="bvc label16",
                addr_mode=AddressModes.Relative,
                ),
    # eor [0xaa],y        ;51 aa      Indirect Y
    Instruction(opcode=0x51,
                template="eor [0xaa],y",
                addr_mode=AddressModes.IndirectY,
                ),
    # .byte 0x52          ;52         Illegal
    Instruction(opcode=0x52,
                template=".byte 0x52",
                addr_mode=AddressModes.Illegal,
                ),
    # bbc 2,a,label17     ;53 fe      Accumulator Bit Relative
    Instruction(opcode=0x53,
                template="bbc 2,a,label17",
                addr_mode=AddressModes.AccumulatorBitRelative,
                ),
    # .byte 0x54          ;54         Illegal
    Instruction(opcode=0x54,
                template=".byte 0x54",
                addr_mode=AddressModes.Illegal,
                ),
    # eor 0xaa,x          ;55 aa      Zero Page X
    Instruction(opcode=0x55,
                template="eor 0xaa,x",
                addr_mode=AddressModes.ZeroPageX,
                ),
    # lsr 0xaa,x          ;56 aa      Zero Page X
    Instruction(opcode=0x56,
                template="lsr 0xaa,x",
                addr_mode=AddressModes.ZeroPageX,
                ),
    # bbc 2,0xaa,label18  ;57 aa fd   Zero Page Bit Relative
    Instruction(opcode=0x57,
                template="bbc 2,0xaa,label18",
                addr_mode=AddressModes.ZeroPageBitRelative,
                ),
    # cli                 ;58         Implied
    Instruction(opcode=0x58,
                template="cli",
                addr_mode=AddressModes.Implied,
                ),
    # eor 0xaabb,y        ;59 bb aa   Absolute Y
    Instruction(opcode=0x59,
                template="eor 0xaabb,y",
                addr_mode=AddressModes.AbsoluteY,
                ),
    # .byte 0x5a          ;5a         Illegal
    Instruction(opcode=0x5a,
                template=".byte 0x5a",
                addr_mode=AddressModes.Illegal,
                ),
    # clb 2,a             ;5b         Accumulator Bit
    Instruction(opcode=0x5b,
                template="clb 2,a",
                addr_mode=AddressModes.AccumulatorBit,
                ),
    # .byte 0x5c          ;5c         Illegal
    Instruction(opcode=0x5c,
                template=".byte 0x5c",
                addr_mode=AddressModes.Illegal,
                ),
    # eor 0xaabb,x        ;5d bb aa   Absolute X
    Instruction(opcode=0x5d,
                template="eor 0xaabb,x",
                addr_mode=AddressModes.AbsoluteX,
                ),
    # lsr 0xaabb,x        ;5e bb aa   Absolute X
    Instruction(opcode=0x5e,
                template="lsr 0xaabb,x",
                addr_mode=AddressModes.AbsoluteX,
                ),
    # clb 2,0xaa          ;5f aa      Zero Page Bit
    Instruction(opcode=0x5f,
                template="clb 2,0xaa",
                addr_mode=AddressModes.ZeroPageBit,
                ),
    # rts                 ;60         Implied
    Instruction(opcode=0x60,
                template="clb 2,0xaa",
                addr_mode=AddressModes.Implied,
                ),
    # adc [0xaa,x]        ;61 aa      Indirect X
    Instruction(opcode=0x61,
                template="adc [0xaa,x]",
                addr_mode=AddressModes.IndirectX,
                ),
    # mul 0xaa,x          ;62 aa      Zero Page X
    Instruction(opcode=0x62,
                template="mul 0xaa,x",
                addr_mode=AddressModes.ZeroPageX,
                ),
    # bbs 3,a,label19     ;63 fe      Accumulator Bit Relative
    Instruction(opcode=0x63,
                template="bbs 3,a,label19",
                addr_mode=AddressModes.AccumulatorBitRelative,
                ),
    # tst 0xaa            ;64 aa      Zero Page
    Instruction(opcode=0x64,
                template="tst 0xaa",
                addr_mode=AddressModes.ZeroPage,
                ),
    # adc 0xaa            ;65 aa      Zero Page
    Instruction(opcode=0x65,
                template="adc 0xaa",
                addr_mode=AddressModes.ZeroPage,
                ),
    # ror 0xaa            ;66 aa      Zero Page
    Instruction(opcode=0x66,
                template="ror 0xaa",
                addr_mode=AddressModes.ZeroPage,
                ),
    # bbs 3,0xaa,label20  ;67 aa fd   Zero Page Bit Relative
    Instruction(opcode=0x67,
                template="bbs 3,0xaa,label20",
                addr_mode=AddressModes.ZeroPageBitRelative,
                ),
    # pla                 ;68         Implied
    Instruction(opcode=0x68,
                template="pla",
                addr_mode=AddressModes.Implied,
                ),
    # adc #0xaa           ;69 aa      Immediate
    Instruction(opcode=0x69,
                template="adc #0xaa",
                addr_mode=AddressModes.Immediate,
                ),
    # ror a               ;6a         Implied
    Instruction(opcode=0x6a,
                template="ror a",
                addr_mode=AddressModes.Implied,
                ),
    # seb 3,a             ;6b         Accumulator Bit
    Instruction(opcode=0x6b,
                template="seb 3,a",
                addr_mode=AddressModes.AccumulatorBit,
                ),
    # jmp [0xaabb]        ;6c bb aa   Indirect Absolute
    Instruction(opcode=0x6c,
                template="jmp [0xaabb]",
                addr_mode=AddressModes.IndirectAbsolute,
                ),
    # adc 0xaabb          ;6d bb aa   Absolute
    Instruction(opcode=0x6d,
                template="adc 0xaabb",
                addr_mode=AddressModes.Absolute,
                ),
    # ror 0xaabb          ;6e bb aa   Absolute
    Instruction(opcode=0x6e,
                template="ror 0xaabb",
                addr_mode=AddressModes.Absolute,
                ),
    # seb 3,0xaa          ;6f aa      Zero Page Bit
    Instruction(opcode=0x6f,
                template="seb 3,0xaa",
                addr_mode=AddressModes.ZeroPageBit,
                ),
    # bvs label21         ;70 fe      Relative
    Instruction(opcode=0x70,
                template="bvs label21",
                addr_mode=AddressModes.Relative,
                ),
    # adc [0xaa],y        ;71 aa      Indirect Y
    Instruction(opcode=0x71,
                template="adc [0xaa],y",
                addr_mode=AddressModes.IndirectY,
                ),
    # .byte 0x72          ;72         Illegal
    Instruction(opcode=0x72,
                template=".byte 72",
                addr_mode=AddressModes.Illegal,
                ),
    # bbc 3,a,label22     ;73 fe      Accumulator Bit Relative
    Instruction(opcode=0x73,
                template="bbc 3,a,label22",
                addr_mode=AddressModes.AccumulatorBitRelative,
                ),
    # .byte 0x74          ;74         Illegal
    Instruction(opcode=0x74,
                template=".byte 0x74",
                addr_mode=AddressModes.Illegal,
                ),
    # adc 0xaa,x          ;75 aa      Zero Page X
    Instruction(opcode=0x75,
                template="adc 0xaa,x",
                addr_mode=AddressModes.ZeroPageX,
                ),
    # ror 0xaa,x          ;76 aa      Zero Page X
    Instruction(opcode=0x76,
                template="ror 0xaa,x",
                addr_mode=AddressModes.ZeroPageX,
                ),
    # bbc 3,0xaa,label23  ;77 aa fd   Zero Page Bit Relative
    Instruction(opcode=0x77,
                template="bbc 3,0xaa,label23",
                addr_mode=AddressModes.ZeroPageBitRelative,
                ),
    # sei                 ;78         Implied
    Instruction(opcode=0x78,
                template="sei",
                addr_mode=AddressModes.Implied,
                ),
    # adc 0xaabb,y        ;79 bb aa   Absolute Y
    Instruction(opcode=0x79,
                template="adc 0xaabb,y",
                addr_mode=AddressModes.AbsoluteY,
                ),
    # .byte 0x7a          ;7a         Illegal
    Instruction(opcode=0x7a,
                template=".byte 0x7a",
                addr_mode=AddressModes.Illegal,
                ),
    # clb 3,a             ;7b         Accumulator Bit
    Instruction(opcode=0x7b,
                template="clb 3,a",
                addr_mode=AddressModes.Illegal,
                ),
    # .byte 0x7c          ;7c         Illegal
    Instruction(opcode=0x7c,
                template=".byte 0x7c",
                addr_mode=AddressModes.Illegal,
                ),
    # adc 0xaabb,x        ;7d bb aa   Absolute X
    Instruction(opcode=0x7d,
                template="adc 0xaabb,x",
                addr_mode=AddressModes.AbsoluteX,
                ),
    # ror 0xaabb,x        ;7e bb aa   Absolute X
    Instruction(opcode=0x7e,
                template="ror 0xaabb,x",
                addr_mode=AddressModes.AbsoluteX,
                ),
    # clb 3,0xaa          ;7f aa      Zero Page Bit
    Instruction(opcode=0x7f,
                template="clb 3,0xaa",
                addr_mode=AddressModes.ZeroPageBit,
                ),
    # bra label24         ;80 fe      Relative
    Instruction(opcode=0x80,
                template="bra label24",
                addr_mode=AddressModes.Relative,
                ),
    # sta [0xaa,x]        ;81 aa      Indirect X
    Instruction(opcode=0x81,
                template="sta [0xaa,x]",
                addr_mode=AddressModes.IndirectX,
                ),
    # rrf 0xaa            ;82 aa      Zero Page
    Instruction(opcode=0x82,
                template="rrf 0xaa",
                addr_mode=AddressModes.ZeroPage,
                ),
    # bbs 4,a,label25     ;83 fe      Accumulator Bit Relative
    Instruction(opcode=0x83,
                template="bbs 4,a,label25",
                addr_mode=AddressModes.AccumulatorBitRelative,
                ),
    # sty 0xaa            ;84 aa      Zero Page
    Instruction(opcode=0x84,
                template="sty 0xaa",
                addr_mode=AddressModes.ZeroPage,
                ),
    # sta 0xaa            ;85 aa      Zero Page
    Instruction(opcode=0x85,
                template="sta 0xaa",
                addr_mode=AddressModes.ZeroPage,
                ),
    # stx 0xaa            ;86 aa      Zero Page
    Instruction(opcode=0x86,
                template="stx 0xaa",
                addr_mode=AddressModes.ZeroPage,
                ),
    # bbs 4,0xaa,label26  ;87 aa fd   Zero Page Bit Relative
    Instruction(opcode=0x87,
                template="bbs 4,0xaa,label26",
                addr_mode=AddressModes.ZeroPageBitRelative,
                ),
    # dey                 ;88         Implied
    Instruction(opcode=0x88,
                template="dey",
                addr_mode=AddressModes.Implied,
                ),
    # .byte 0x89          ;89         Illegal
    Instruction(opcode=0x89,
                template=".byte 0x89",
                addr_mode=AddressModes.Illegal,
                ),
    # txa                 ;8a         Implied
    Instruction(opcode=0x8a,
                template="txa",
                addr_mode=AddressModes.Implied,
                ),
    # seb 4,a             ;8b         Accumulator Bit
    Instruction(opcode=0x8b,
                template="seb 4,a",
                addr_mode=AddressModes.AccumulatorBit,
                ),
    # sty 0xaabb          ;8c bb aa   Accumulator
    Instruction(opcode=0x8c,
                template="sty 0xaabb",
                addr_mode=AddressModes.Accumulator,
                ),
    # sta 0xaabb          ;8d bb aa   Accumulator
    Instruction(opcode=0x8d,
                template="sta 0xaabb",
                addr_mode=AddressModes.Accumulator,
                ),
    # stx 0xaabb          ;8e bb aa   Accumulator
    Instruction(opcode=0x8e,
                template="stx 0xaabb",
                addr_mode=AddressModes.Accumulator,
                ),
    # seb 4,0xaa          ;8f aa      Zero Page Bit
    Instruction(opcode=0x8f,
                template="seb 4,0xaa",
                addr_mode=AddressModes.ZeroPageBit,
                ),
    # bcc label27         ;90 fe      Relative
    Instruction(opcode=0x90,
                template="bcc label27",
                addr_mode=AddressModes.Relative,
                ),
    # sta [0xaa],y        ;91 aa      Indirect Y
    Instruction(opcode=0x91,
                template="sta [0xaa],y",
                addr_mode=AddressModes.IndirectY,
                ),
    # .byte 0x92          ;92         Illegal
    Instruction(opcode=0x92,
                template=".byte 0x92",
                addr_mode=AddressModes.Illegal,
                ),
    # bbc 4,a,label28     ;93 fe      Accumulator Bit Relative
    Instruction(opcode=0x93,
                template="bbc 4,a,label28",
                addr_mode=AddressModes.AccumulatorBitRelative,
                ),
    # sty 0xaa,x          ;94 aa      Zero Page X
    Instruction(opcode=0x94,
                template="sty 0xaa,x",
                addr_mode=AddressModes.ZeroPageX,
                ),
    # sta 0xaa,x          ;95 aa      Zero Page X
    Instruction(opcode=0x95,
                template="sta 0xaa,x",
                addr_mode=AddressModes.ZeroPageX,
                ),
    # stx 0xaa,y          ;96 aa      Zero Page Y
    Instruction(opcode=0x96,
                template="stx 0xaa,y",
                addr_mode=AddressModes.ZeroPageY,
                ),
    # bbc 4,0xaa,label29  ;97 aa fd   Zero Page Bit Relative
    Instruction(opcode=0x97,
                template="bbc 4,0xaa,label29",
                addr_mode=AddressModes.ZeroPageBitRelative,
                ),
    # tya                 ;98         Implied
    Instruction(opcode=0x98,
                template="tya",
                addr_mode=AddressModes.Implied,
                ),
    # sta 0xaabb,y        ;99 bb aa   Absolute Y
    Instruction(opcode=0x99,
                template="sta 0xaabb,y",
                addr_mode=AddressModes.AbsoluteY,
                ),
    # txs                 ;9a         Implied
    Instruction(opcode=0x9a,
                template="txs",
                addr_mode=AddressModes.Implied,
                ),
    # clb 4,a             ;9b         Accumulator Bit
    Instruction(opcode=0x9b,
                template="clb 4,a",
                addr_mode=AddressModes.AccumulatorBit,
                ),
    # .byte 0x9c          ;9c         Illegal
    Instruction(opcode=0x9c,
                template=".byte 0x9c",
                addr_mode=AddressModes.Illegal,
                ),
    # sta 0xaabb,x        ;9d bb aa   Absolute X
    Instruction(opcode=0x9d,
                template="sta 0xaabb,x",
                addr_mode=AddressModes.AbsoluteX,
                ),
    # .byte 0x9e          ;9e         Illegal
    Instruction(opcode=0x9e,
                template=".byte 0x9e",
                addr_mode=AddressModes.Illegal,
                ),
    # clb 4,0xaa          ;9f aa      Zero Page Bit
    Instruction(opcode=0x9f,
                template="clb 4,0xaa",
                addr_mode=AddressModes.ZeroPageBit,
                ),
    # ldy #0xaa           ;a0 aa      Immediate
    Instruction(opcode=0xa0,
                template="ldy #0xaa",
                addr_mode=AddressModes.Immediate,
                ),
    # lda [0xaa,x]        ;a1 aa      Indirect X
    Instruction(opcode=0xa1,
                template="lda [0xaa,x]",
                addr_mode=AddressModes.IndirectX,
                ),
    # ldx #0xaa           ;a2 aa      Immediate
    Instruction(opcode=0xa2,
                template="ldx #0xaa",
                addr_mode=AddressModes.Immediate,
                ),
    # bbs 5,a,label30     ;a3 fe      Accumulator Bit Relative
    Instruction(opcode=0xa3,
                template="bbs 5,a,label30",
                addr_mode=AddressModes.AccumulatorBitRelative,
                ),
    # ldy 0xaa            ;a4 aa      Zero Page
    Instruction(opcode=0xa4,
                template="ldy 0xaa",
                addr_mode=AddressModes.ZeroPage,
                ),
    # lda 0xaa            ;a5 aa      Zero Page
    Instruction(opcode=0xa5,
                template="lda 0xaa",
                addr_mode=AddressModes.ZeroPage,
                ),
    # ldx 0xaa            ;a6 aa      Zero Page
    Instruction(opcode=0xa6,
                template="ldx 0xaa",
                addr_mode=AddressModes.ZeroPage,
                ),
    # bbs 5,0xaa,label31  ;a7 aa fd   Accumulator Bit Relative
    Instruction(opcode=0xa7,
                template="bbs 5,0xaa,label31",
                addr_mode=AddressModes. AccumulatorBitRelative,
                ),
    # tay                 ;a8         Implied
    Instruction(opcode=0xa8,
                template="tay",
                addr_mode=AddressModes.Implied,
                ),
    # lda #0xaa           ;a9 aa      Immediate
    Instruction(opcode=0xa9,
                template="lda #0xaa",
                addr_mode=AddressModes.Immediate,
                ),
    # tax                 ;aa         Implied
    Instruction(opcode=0xaa,
                template="tax",
                addr_mode=AddressModes.Implied,
                ),
    # seb 5,a             ;ab         Accumulator Bit
    Instruction(opcode=0xab,
                template="seb 5,a",
                addr_mode=AddressModes.AccumulatorBit,
                ),
    # ldy 0xaabb          ;ac bb aa   Absolute
    Instruction(opcode=0xac,
                template="ldy 0xaabb",
                addr_mode=AddressModes.Absolute,
                ),
    # lda 0xaabb          ;ad bb aa   Absolute
    Instruction(opcode=0xad,
                template="lda 0xaabb",
                addr_mode=AddressModes.Absolute,
                ),
    # ldx 0xaabb          ;ae bb aa   Absolute
    Instruction(opcode=0xae,
                template="ldx 0xaabb",
                addr_mode=AddressModes.Absolute,
                ),
    # seb 5,0xaa          ;af aa      Zero Page Bit
    Instruction(opcode=0xaf,
                template="seb 5,0xaa",
                addr_mode=AddressModes.ZeroPageBit,
                ),
    # bcs label32         ;b0 fe      Relative
    Instruction(opcode=0xb0,
                template="bcs label32",
                addr_mode=AddressModes.Relative,
                ),
    # lda [0xaa],y        ;b1 aa      Indirect Y
    Instruction(opcode=0xb1,
                template="lda [0xaa],y",
                addr_mode=AddressModes.IndirectY,
                ),
    # jmp [0xaa]          ;b2 aa      Zero Page Indirect
    Instruction(opcode=0xb2,
                template="jmp [0xaa]",
                addr_mode=AddressModes.ZeroPageIndirect,
                ),
    # bbc 5,a,label33     ;b3 fe      Accumulator Bit Relative
    Instruction(opcode=0xb3,
                template="bbc 5,a,label33",
                addr_mode=AddressModes.AccumulatorBitRelative,
                ),
    # ldy 0xaa,x          ;b4 aa      Zero Page X
    Instruction(opcode=0xb4,
                template="ldy 0xaa,x",
                addr_mode=AddressModes.ZeroPageX,
                ),
    # lda 0xaa,x          ;b5 aa      Zero Page X
    Instruction(opcode=0xb5,
                template="lda 0xaa,x",
                addr_mode=AddressModes.ZeroPageX,
                ),
    # ldx 0xaa,y          ;b6 aa      Zero Page Y
    Instruction(opcode=0xb6,
                template="ldx 0xaa,y",
                addr_mode=AddressModes.ZeroPageY,
                ),
    # bbc 5,0xaa,label34  ;b7 aa fd   Zero Page Bit Relative
    Instruction(opcode=0xb7,
                template="bbc 5,0xaa,label34",
                addr_mode=AddressModes.ZeroPageBitRelative,
                ),
    # clv                 ;b8         Implied
    Instruction(opcode=0xb8,
                template="clv",
                addr_mode=AddressModes.Implied,
                ),
    # lda 0xaabb,y        ;b9 bb aa   Absolute Y
    Instruction(opcode=0xb9,
                template="lda 0xaabb,y",
                addr_mode=AddressModes.AbsoluteY,
                ),
    # tsx                 ;ba         Implied
    Instruction(opcode=0xba,
                template="tsx",
                addr_mode=AddressModes.Implied,
                ),
    # clb 5,a             ;bb         Accumulator Bit
    Instruction(opcode=0xbb,
                template="clb 5,a",
                addr_mode=AddressModes.AccumulatorBit,
                ),
    # ldy 0xaabb,x        ;bc bb aa   Absolute X
    Instruction(opcode=0xbc,
                template="ldy 0xaabb,x",
                addr_mode=AddressModes.AbsoluteX,
                ),
    # lda 0xaabb,x        ;bd bb aa   Absolute X
    Instruction(opcode=0xbd,
                template="lda 0xaabb,x",
                addr_mode=AddressModes.AbsoluteX,
                ),
    # ldx 0xaabb,y        ;be bb aa   Absolute Y
    Instruction(opcode=0xbe,
                template="ldx 0xaabb,y",
                addr_mode=AddressModes.AbsoluteY,
                ),
    # clb 5,0xaa          ;bf aa      Zero Page Bit
    Instruction(opcode=0xbf,
                template="clb 5,0xaa",
                addr_mode=AddressModes.ZeroPageBit,
                ),
    # cpy #0xaa           ;c0 aa      Immediate
    Instruction(opcode=0xc0,
                template="cpy #0xaa",
                addr_mode=AddressModes.Immediate,
                ),
    # cmp [0xaa,x]        ;c1 aa      Indirect X
    Instruction(opcode=0xc1,
                template="cmp [0xaa,x]",
                addr_mode=AddressModes.IndirectX,
                ),
    # wit                 ;c2         Implied
    Instruction(opcode=0xc2,
                template="wit",
                addr_mode=AddressModes.Implied,
                ),
    # bbs 6,a,label35     ;c3 fe      Accumulator Bit Relative
    Instruction(opcode=0xc3,
                template="bbs 6,a,label35",
                addr_mode=AddressModes.AccumulatorBitRelative,
                ),
    # cpy 0xaa            ;c4 aa      Zero Page
    Instruction(opcode=0xc4,
                template="cpy 0xaa",
                addr_mode=AddressModes.ZeroPage,
                ),
    # cmp 0xaa            ;c5 aa      Zero Page
    Instruction(opcode=0xc5,
                template="cmp 0xaa",
                addr_mode=AddressModes.ZeroPage,
                ),
    # dec 0xaa            ;c6 aa      Zero Page
    Instruction(opcode=0xc6,
                template="dec 0xaa",
                addr_mode=AddressModes.ZeroPage,
                ),
    # bbs 6,0xaa,label36  ;c7 aa fd   Zero Page Bit Relative
    Instruction(opcode=0xc7,
                template="bbs 6,0xaa,label36",
                addr_mode=AddressModes.ZeroPageBitRelative,
                ),
    # iny                 ;c8         Implied
    Instruction(opcode=0xc8,
                template="iny",
                addr_mode=AddressModes.Implied,
                ),
    # cmp #0xaa           ;c9 aa      Immediate
    Instruction(opcode=0xc9,
                template="cmp #0xaa",
                addr_mode=AddressModes.Immediate,
                ),
    # dex                 ;ca         Implied
    Instruction(opcode=0xca,
                template="dex",
                addr_mode=AddressModes.Implied,
                ),
    # seb 6,a             ;cb         Accumulator Bit
    Instruction(opcode=0xcb,
                template="seb 6,a",
                addr_mode=AddressModes.AccumulatorBit,
                ),
    # cpy 0xaabb          ;cc bb aa   Absolute
    Instruction(opcode=0xcc,
                template="cpy 0xaabb",
                addr_mode=AddressModes.Absolute,
                ),
    # cmp 0xaabb          ;cd bb aa   Absolute
    Instruction(opcode=0xcd,
                template="cmp 0xaabb",
                addr_mode=AddressModes.Absolute,
                ),
    # dec 0xaabb          ;ce bb aa   Absolute
    Instruction(opcode=0xce,
                template="dec 0xaabb",
                addr_mode=AddressModes.Absolute,
                ),
    # seb 6,0xaa          ;cf aa      Zero Page Bit
    Instruction(opcode=0xcf,
                template="seb 6,0xaa",
                addr_mode=AddressModes.ZeroPageBit,
                ),
    # bne label37         ;d0 fe      Relative
    Instruction(opcode=0xd0,
                template="bne label37",
                addr_mode=AddressModes.Relative,
                ),
    # cmp [0xaa],y        ;d1 aa      Indirect Y
    Instruction(opcode=0xd1,
                template="cmp [0xaa],y",
                addr_mode=AddressModes.IndirectY,
                ),
    # .byte 0xd2          ;d2         Illegal
    Instruction(opcode=0xd2,
                template=".byte 0xd2",
                addr_mode=AddressModes.Illegal,
                ),
    # bbc 6,a,label38     ;d3 fe      Accumulator Bit Relative
    Instruction(opcode=0xd3,
                template="bbc 6,a,label38",
                addr_mode=AddressModes.AccumulatorBitRelative,
                ),
    # .byte 0xd4          ;d4         Illegal
    Instruction(opcode=0xd4,
                template=".byte 0xd4",
                addr_mode=AddressModes.Illegal,
                ),
    # cmp 0xaa,x          ;d5 aa      Zero Page X
    Instruction(opcode=0xd5,
                template="cmp 0xaa,x",
                addr_mode=AddressModes.ZeroPageX,
                ),
    # dec 0xaa,x          ;d6 aa      Zero Page X
    Instruction(opcode=0xd6,
                template="dec 0xaa,x",
                addr_mode=AddressModes.ZeroPageX,
                ),
    # bbc 6,0xaa,label39  ;d7 aa fd   Zero Page Bit Relative
    Instruction(opcode=0xd7,
                template="bbc 6,0xaa,label39",
                addr_mode=AddressModes.ZeroPageBitRelative,
                ),
    # cld                 ;d8         Implied
    Instruction(opcode=0xd8,
                template="cld",
                addr_mode=AddressModes.Implied,
                ),
    # cmp 0xaabb,y        ;d9 bb aa   Absolute Y
    Instruction(opcode=0xd9,
                template="cmp 0xaabb,y",
                addr_mode=AddressModes.AbsoluteY,
                ),
    # .byte 0xda          ;da         Illegal
    Instruction(opcode=0xda,
                template=".byte 0xda",
                addr_mode=AddressModes.Illegal,
                ),
    # clb 6,a             ;db         Accumulator Bit
    Instruction(opcode=0xdb,
                template="clb 6,a",
                addr_mode=AddressModes.AccumulatorBit,
                ),
    # .byte 0xdc          ;dc         Illegal
    Instruction(opcode=0xdc,
                template=".byte 0xdc",
                addr_mode=AddressModes.Illegal,
                ),
    # cmp 0xaabb,x        ;dd bb aa   Absolute X
    Instruction(opcode=0xdd,
                template="cmp 0xaabb,x",
                addr_mode=AddressModes.AbsoluteX,
                ),
    # dec 0xaabb,x        ;de bb aa   Absolute X
    Instruction(opcode=0xde,
                template="dec 0xaabb,x",
                addr_mode=AddressModes.AbsoluteX,
                ),
    # clb 6,0xaa          ;df aa      Zero Page Bit
    Instruction(opcode=0xdf,
                template="clb 6,0xaa",
                addr_mode=AddressModes.ZeroPageBit
                ),
    # cpx #0xaa           ;e0 aa      Immediate
    Instruction(opcode=0xe0,
                template="cpx #0xaa",
                addr_mode=AddressModes.Immediate
                ),
    # sbc [0xaa,x]        ;e1 aa      Indirect X
    Instruction(opcode=0xe1,
                template="sbc [0xaa,x]",
                addr_mode=AddressModes.IndirectX
                ),
    # div 0xaa,x          ;e2 aa      Zero Page X
    Instruction(opcode=0xe2,
                template="div 0xaa,x",
                addr_mode=AddressModes.ZeroPageX
                ),
    # bbs 7,a,label40     ;e3 fe      Accumulator Bit Relative
    Instruction(opcode=0xe3,
                template="bbs 7,a,label40",
                addr_mode=AddressModes.AccumulatorBitRelative
                ),
    # cpx 0xaa            ;e4 aa      Zero Page
    Instruction(opcode=0xe4,
                template="cpx 0xaa",
                addr_mode=AddressModes.ZeroPage
                ),
    # sbc 0xaa            ;e5 aa      Zero Page
    Instruction(opcode=0xe5,
                template="sbc 0xaa",
                addr_mode=AddressModes.ZeroPage
                ),
    # inc 0xaa            ;e6 aa      Zero Page
    Instruction(opcode=0xe6,
                template="inc 0xaa",
                addr_mode=AddressModes.ZeroPage
                ),
    # bbs 7,0xaa,label41  ;e7 aa fd   Accumulator Bit Relative
    Instruction(opcode=0xe7,
                template="bbs 7,0xaa,label41",
                addr_mode=AddressModes.AccumulatorBitRelative
                ),
    # inx                 ;e8         Implied
    Instruction(opcode=0xe8,
                template="inx",
                addr_mode=AddressModes.Implied
                ),
    # sbc #0xaa           ;e9 aa      Zero Page
    Instruction(opcode=0xe9,
                template="sbc #0xaa",
                addr_mode=AddressModes.ZeroPage
                ),
    # nop                 ;ea         Implied
    Instruction(opcode=0xea,
                template="nop",
                addr_mode=AddressModes.Implied
                ),
    # seb 7,a             ;eb         Accumulator Bit
    Instruction(opcode=0xeb,
                template="seb 7,a",
                addr_mode=AddressModes.AccumulatorBit
                ),
    # cpx 0xaabb          ;ec bb aa   Absolute
    Instruction(opcode=0xec,
                template="cpx 0xaabb",
                addr_mode=AddressModes.Absolute
                ),
    # sbc 0xaabb          ;ed bb aa   Absolute
    Instruction(opcode=0xed,
                template="sbc 0xaabb",
                addr_mode=AddressModes.Absolute
                ),
    # inc 0xaabb          ;ee bb aa   Absolute
    Instruction(opcode=0xee,
                template="inc 0xaabb",
                addr_mode=AddressModes.Absolute
                ),
    # seb 7,0xaa          ;ef aa      Zero Page Bit
    Instruction(opcode=0xef,
                template="seb 7,0xaa",
                addr_mode=AddressModes.ZeroPageBit
                ),
    # beq label42         ;f0 fe      Relative
    Instruction(opcode=0xf0,
                template="beq label42",
                addr_mode=AddressModes.Relative
                ),
    # sbc [0xaa],y        ;f1 aa      Indirect Y
    Instruction(opcode=0xf1,
                template="sbc [0xaa],y",
                addr_mode=AddressModes.IndirectY
                ),
    # .byte 0xf2          ;f2         Illegal
    Instruction(opcode=0xf2,
                template=".byte 0xf2",
                addr_mode=AddressModes.Illegal
                ),
    # bbc 7,a,label43     ;f3 fe      Accumulator Bit Relative
    Instruction(opcode=0xf3,
                template="bbc 7,a,label43",
                addr_mode=AddressModes.AccumulatorBitRelative
                ),
    # .byte 0xf4          ;f4         Illegal
    Instruction(opcode=0xf4,
                template=".byte 0x4",
                addr_mode=AddressModes.Illegal
                ),
    # sbc 0xaa,x          ;f5 aa      Zero Page X
    Instruction(opcode=0xf5,
                template="sbc 0xaa,x",
                addr_mode=AddressModes.ZeroPageX
                ),
    # inc 0xaa,x          ;f6 aa      Zero Page X
    Instruction(opcode=0xf6,
                template="inc 0xaa,x",
                addr_mode=AddressModes.ZeroPageX
                ),
    # bbc 7,0xaa,label44  ;f7 aa fd   Zero Page Bit Relative
    Instruction(opcode=0xf7,
                template="bbc 7,0xaa,label44",
                addr_mode=AddressModes.ZeroPageBitRelative
                ),
    # sed                 ;f8         Implied
    Instruction(opcode=0xf8,
                template="sed",
                addr_mode=AddressModes.Implied
                ),
    # sbc 0xaabb,y        ;f9 bb aa   Absolute Y
    Instruction(opcode=0xf9,
                template="sed",
                addr_mode=AddressModes.Implied
                ),
    # .byte 0xfa          ;fa         Illegal
    Instruction(opcode=0xfa,
                template=".byte 0xfa",
                addr_mode=AddressModes.Illegal
                ),
    # clb 7,a             ;fb         Accumulator Bit
    Instruction(opcode=0xfb,
                template="clb 7,a",
                addr_mode=AddressModes.AccumulatorBit
                ),
    # .byte 0xfc          ;fc         Illegal
    Instruction(opcode=0xfc,
                template=".byte 0xfc",
                addr_mode=AddressModes.Illegal
                ),
    # sbc 0xaabb,x        ;fd bb aa   Absolute X
    Instruction(opcode=0xfd,
                template="sbc 0xaabb,x",
                addr_mode=AddressModes.AbsoluteX
                ),
    # inc 0xaabb,x        ;fe bb aa   Absolute X
    Instruction(opcode=0xfe,
                template="inc 0xaabb,x",
                addr_mode=AddressModes.AbsoluteX
                ),
    # clb 7,0xaa          ;ff aa      Zero Page Bit
    Instruction(opcode=0xff,
                template="clb 7,0xaa",
                addr_mode=AddressModes.ZeroPageBit
                ),
)
