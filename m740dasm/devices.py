from m740dasm.symbols import Symbol

Devices = {}

# "7450 Group" (e.g. M37450)
Devices["7450"] = {"vector_table":
    [ # Interrupt vector table - "7450 Group"
        0xffe0, # BRK instruction
        0xffe2, # A-D conversion completion
        0xffe4, # Serial I/O transmit
        0xffe6, # Serial I/O receive
        0xffe8, # EV3 (External event)
        0xffea, # EV2 (External event)
        0xffec, # EV1 (External event)
        0xffee, # Timer 3
        0xfff0, # Timer 2
        0xfff2, # Timer 1
        0xfff4, # INT3 (External interrupt)
        0xfff6, # INT2 (External interrupt)
        0xfff8, # INT1 (External interrupt)
        0xfffa, # Output buffer full
        0xfffc, # Input buffer full
        0xfffe, # RESET
    ],
    "symbol_table":
    [ # Symbol Table - "7450 Group"
        # I/O
        Symbol(0x00d0, "P0",      "Port P0"),
        Symbol(0x00d1, "P0D",     "Port P0 directional register"),
        Symbol(0x00d2, "P1",      "Port P1"),
        Symbol(0x00d3, "P1D",     "Port P1 directional register"),
        Symbol(0x00d4, "P2",      "Port P2"),
        Symbol(0x00d5, "P2D",     "Port P2 directional register"),
        Symbol(0x00d6, "P3",      "Port P3"),
        Symbol(0x00d7, "P3D",     "Port P3 directional register"),
        Symbol(0x00d8, "P4",      "Port P4"),
        Symbol(0x00d9, "RESERV",  "Reserved"),
        Symbol(0x00da, "P5",      "Port P5"),
        Symbol(0x00db, "P5D",     "Port P5 directional register"),
        Symbol(0x00dc, "P6",      "Port P6"),
        Symbol(0x00dd, "P6D",     "Port P6 directional register"),
        Symbol(0x00de, "MISRG1",  "Miscellaneous register 1"),
        Symbol(0x00df, "MISRG2",  "Miscellaneous register 2"),
        Symbol(0x00e0, "DA1",     "D-A1 conversion register"),
        Symbol(0x00e1, "DA2",     "D-A2 conversion register"),
        Symbol(0x00e2, "AD",      "A-D conversion register"),
        Symbol(0x00e3, "ADCNT",   "A-D control register"),
        Symbol(0x00e4, "DBB",     "Data bus buffer register"),
        Symbol(0x00e5, "DBBSTS",  "Data bus buffer status register"),
        Symbol(0x00e6, "RTB",     "Receive/Transmit buffer register"),
        Symbol(0x00e7, "SIOSTS",  "Serial I/O status register"),
        Symbol(0x00e8, "SIOCON",  "Serial I/O control register"),
        Symbol(0x00e9, "UARTCON", "UART control register"),
        Symbol(0x00ea, "BRG",     "Baud rate generator"),
        Symbol(0x00eb, "PWML",    "PWM register (low-order)"),
        Symbol(0x00ec, "PWMH",    "PWM register (high-order)"),
        Symbol(0x00ed, "T1CON",   "Timer 1 control register"),
        Symbol(0x00ee, "T2CON",   "Timer 2 control register"),
        Symbol(0x00ef, "T3CON",   "Timer 3 control register"),
        Symbol(0x00f0, "T1L",     "Timer 1 register (low-order)"),
        Symbol(0x00f1, "T1H",     "Timer 1 register (high-order)"),
        Symbol(0x00f2, "T1LATL",  "Timer 1 latch (low-order)"),
        Symbol(0x00f3, "T1LATH",  "Timer 1 latch (high-order)"),
        Symbol(0x00f4, "T2L",     "Timer 2 register (low-order)"),
        Symbol(0x00f5, "T2H",     "Timer 2 register (high-order)"),
        Symbol(0x00f6, "T2LATL",  "Timer 2 latch (low-order)"),
        Symbol(0x00f7, "T2LATH",  "Timer 2 latch (high-order)"),
        Symbol(0x00f8, "T3L",     "Timer 3 register (low-order)"),
        Symbol(0x00f9, "T3H",     "Timer 3 register (high-order)"),
        Symbol(0x00fa, "T3LATL",  "Timer 3 latch (low-order)"),
        Symbol(0x00fb, "T3LATH",  "Timer 3 latch (high-order)"),
        Symbol(0x00fc, "IREQ1",   "Interrupt request register 1"),
        Symbol(0x00fd, "IREQ2",   "Interrupt request register 2"),
        Symbol(0x00fe, "ICON1",   "Interrupt control register 1"),
        Symbol(0x00ff, "ICON2",   "Interrupt control register 2"),

        # vectors
        Symbol(0xfffe, "RESET",           "Reset vector"),
        Symbol(0xfffc, "INT_FFFC_IBF",    "Input buffer full (IBF)"),
        Symbol(0xfffa, "INT_FFFA_OBE",    "Output buffer empty (OBE)"),
        Symbol(0xfff8, "INT_FFF8_INT1",   "INT1 (External interrupt 1)"),
        Symbol(0xfff6, "INT_FFF6_INT2",   "INT2 (External interrupt 2)"),
        Symbol(0xfff4, "INT_FFF4_INT3",   "INT3 (External interrupt 3)"),
        Symbol(0xfff2, "INT_FFF2_TIMER1", "Timer 1"),
        Symbol(0xfff0, "INT_FFF0_TIMER2", "Timer 2"),
        Symbol(0xffee, "INT_FFEE_TIMER3", "Timer 3"),
        Symbol(0xffec, "INT_FFEC_EVENT1", "EV1 (External event 1)"),
        Symbol(0xffea, "INT_FFEA_EVENT2", "EV2 (External event 2)"),
        Symbol(0xffe8, "INT_FFE8_EVENT3", "EV3 (External event 3)"),
        Symbol(0xffe6, "INT_FFE6_SIORX",  "Serial I/O receive"),
        Symbol(0xffe4, "INT_FFE4_SIOTX",  "Serial I/O transmit"),
        Symbol(0xffe2, "INT_FFE2_ADC",    "A-D conversion completion flag"),
        Symbol(0xffe0, "INT_BRK",         "BRK instruction"),
    ]
}
# Add an "alias" for M37450
Devices["M37450"] = Devices["7450"]

# "7451 Group" (e.g. M37451)
Devices["7451"] = Devices["7450"].copy()
Devices["7451"]["symbol_table"] = Devices["7450"]["symbol_table"][:]
Devices["7451"]["symbol_table"][8] = Symbol(0x00d8, "P4",      "Port P4 / PWM prescaler latch")
Devices["7451"]["symbol_table"][9] = Symbol(0x00d9, "AFD",     "Additional function register")
# Add an "alias" for M37451
Devices["M37451"] = Devices["7451"]

# M3886
Devices["M3886"] = {"vector_table":
    [ # Vector table - M3886
        # brk
        0xffdc,
        # interrupts
        0xffde, 0xffe0, 0xffe2, 0xffe4, 0xffe6, 0xffe8, 0xffea, 0xffec,
        0xffee, 0xfff0, 0xfff2, 0xfff4, 0xfff6, 0xfff8, 0xfffa,
        # reset
        0xfffc,
    ],
    "symbol_table":
    [ # Symbol Table - M3886
        # i/o
        Symbol(0x0000, "P0", 	    "Port P0"),
        Symbol(0x0001, "P0D",       "Port P0 direction register"),
        Symbol(0x0002, "P1", 	    "Port P1"),
        Symbol(0x0003, "P1D",       "Port P1 direction register"),
        Symbol(0x0004, "P2", 	    "Port P2"),
        Symbol(0x0005, "P2D",       "Port P2 direction register"),
        Symbol(0x0006, "P3", 	    "Port P3"),
        Symbol(0x0007, "P3D",       "Port P3 direction register"),
        Symbol(0x0008, "P4", 	    "Port P4"),
        Symbol(0x0009, "P4D",       "Port P4 direction register"),
        Symbol(0x000a, "P5", 	    "Port P5"),
        Symbol(0x000b, "P5D",       "Port P5 direction register"),
        Symbol(0x000c, "P6", 	    "Port P6"),
        Symbol(0x000d, "P6D",       "Port P6 direction register"),
        Symbol(0x000e, "P7", 	    "Port P7"),
        Symbol(0x000f, "P7D",       "Port P7 direction register"),
        Symbol(0x0010, "P8_P4I", 	"Port P8 / Port P4 input register"),
        Symbol(0x0011, "P8D_P7I",   "Port P8 direction register / Port P7 input register"),
        Symbol(0x0012, "S0", 	    "I2C data shift register"),
        Symbol(0x0013, "S0D", 	    "I2C address register"),
        Symbol(0x0014, "S1", 	    "I2C status register"),
        Symbol(0x0015, "S1D",       "I2C control register"),
        Symbol(0x0016, "S2", 	    "I2C clock control register"),
        Symbol(0x0017, "S2D",       "I2C start/stop condition control register"),
        Symbol(0x0018, "TB_RB", 	"Transmit/Receive buffer register"),
        Symbol(0x0019, "SIO1STS",   "Serial I/O1 status register"),
        Symbol(0x001a, "SIO1CON",   "Serial I/O1 control register"),
        Symbol(0x001b, "UARTCON",   "UART control register"),
        Symbol(0x001c, "BRG",       "Baud rate generator"),
        Symbol(0x001d, "SIO2CON",   "Serial I/O2 control register"),
        Symbol(0x001e, "WDTCON", 	"Watchdog timer control register"),
        Symbol(0x001f, "SIO2", 	    "Serial I/O2 register"),
        Symbol(0x0020, "PRE12", 	"Prescaler 12"),
        Symbol(0x0021, "T1", 	    "Timer 1"),
        Symbol(0x0022, "T2", 	    "Timer 2"),
        Symbol(0x0023, "TM", 	    "Timer XY mode register"),
        Symbol(0x0024, "PREX", 	    "Prescaler X"),
        Symbol(0x0025, "TX", 	    "Timer X"),
        Symbol(0x0026, "PREY", 	    "Prescaler Y"),
        Symbol(0x0027, "TY", 	    "Timer Y"),
        Symbol(0x0028, "DBB0", 	    "Data bus buffer register 0"),
        Symbol(0x0029, "DBBSTS0",   "Data bus buffer status register 0"),
        Symbol(0x002a, "DBBCON", 	"Data bus buffer control register"),
        Symbol(0x002b, "DBB1", 	    "Data bus buffer register 1"),
        Symbol(0x002c, "DBBSTS1",   "Data bus buffer status register 1"),
        Symbol(0x002d, "CMPD", 	    "Comparator data register"),
        Symbol(0x002e, "PCTL1", 	"Port control register 1"),
        Symbol(0x002f, "PCTL2", 	"Port control register 2"),
        Symbol(0x0030, "PWM0H", 	"PWM0H register"),
        Symbol(0x0031, "PWM0L", 	"PWM0L register"),
        Symbol(0x0032, "PWM1H", 	"PWM1H register"),
        Symbol(0x0033, "PWM1L", 	"PWM1L register"),
        Symbol(0x0034, "ADCON", 	"AD/DA control register"),
        Symbol(0x0035, "AD1", 	    "A-D conversion register 1"),
        Symbol(0x0036, "DA1", 	    "D-A1 conversion register"),
        Symbol(0x0037, "DA2", 	    "D-A2 conversion register"),
        Symbol(0x0038, "AD2", 	    "A-D conversion register 2"),
        Symbol(0x0039, "INTSEL", 	"Interrupt source selection register"),
        Symbol(0x003a, "INTEDGE",   "Interrupt edge selection register"),
        Symbol(0x003b, "CPUM", 	    "CPU mode register"),
        Symbol(0x003c, "IREQ1", 	"Interrupt request register 1"),
        Symbol(0x003d, "IREQ2", 	"Interrupt request register 2"),
        Symbol(0x003e, "ICON1", 	"Interrupt control register 1"),
        Symbol(0x003f, "ICON2", 	"Interrupt control register 2"),
        Symbol(0x0ffe, "FCON", 	    "Flash memory control register"),
        Symbol(0x0fff, "FCMD", 	    "Flash command register"),

        # vectors
        Symbol(0xfffc, "RESET",     "Reset vector"),
        Symbol(0xfffa, "INT_FFFA",  "INT0 / Input buffer full (IBF)"),
        Symbol(0xfff8, "INT_FFF8",  "INT1 / Output buffer empty (OBE)"),
        Symbol(0xfff6, "INT_FFF6",  "Serial I/O 1 reception"),
        Symbol(0xfff4, "INT_FFF4",  "Serial I/O 2 transmission / SCL, SDA"),
        Symbol(0xfff2, "INT_FFF2",  "Timer X"),
        Symbol(0xfff0, "INT_FFF0",  "Timer Y"),
        Symbol(0xffee, "INT_FFEE",  "Timer 1"),
        Symbol(0xffec, "INT_FFEC",  "Timer 2"),
        Symbol(0xffea, "INT_FFEA",  "CNTR0 / SCL, SDA"),
        Symbol(0xffe8, "INT_FFE8",  "CNTR1 / Key-on wake-up"),
        Symbol(0xffe6, "INT_FFE6",  "Serial I/O 2 / I2C"),
        Symbol(0xffe4, "INT_FFE4",  "INT2 / I2C"),
        Symbol(0xffe2, "INT_FFE2",  "INT3"),
        Symbol(0xffe0, "INT_FFE0",  "INT4"),
        Symbol(0xffde, "INT_FFDE",  "A-D converter / Key-on wake-up"),
        Symbol(0xffdc, "INT_BRK",   "BRK instruction interrupt"),
    ]
}
# "3807 Group" (e.g. M38078)
# Source: https://www.renesas.com/en/document/dst/3807-group-datasheet
Devices["M3807"] = {"vector_table":
    [ # Vector table - M3807
        # brk
        0xffdc,
        # interrupts
        0xffde, 0xffe0, 0xffe2, 0xffe4, 0xffe6, 0xffe8, 0xffea, 0xffec,
        0xffee, 0xfff0, 0xfff2, 0xfff4, 0xfff6, 0xfff8, 0xfffa,
        # reset
        0xfffc,
    ],
    "symbol_table":
    [ # Symbol Table - M3807
        # i/o
        Symbol(0x0000, "P0",        "Port P0"),
        Symbol(0x0001, "P0D",       "Port P0 direction register"),
        Symbol(0x0002, "P1",        "Port P1"),
        Symbol(0x0003, "P1D",       "Port P1 direction register"),
        Symbol(0x0004, "P2",        "Port P2"),
        Symbol(0x0005, "P2D",       "Port P2 direction register"),
        Symbol(0x0006, "P3",        "Port P3"),
        Symbol(0x0007, "P3D",       "Port P3 direction register"),
        Symbol(0x0008, "P4",        "Port P4"),
        Symbol(0x0009, "P4D",       "Port P4 direction register"),
        Symbol(0x000a, "P5",        "Port P5"),
        Symbol(0x000b, "P5D",       "Port P5 direction register"),
        Symbol(0x000c, "P6",        "Port P6"),
        Symbol(0x000d, "P6D",       "Port P6 direction register"),
        Symbol(0x000e, "P7",        "Port P7"),
        Symbol(0x000f, "P7D",       "Port P7 direction register"),
        Symbol(0x0010, "P8",        "Port P8"),
        Symbol(0x0011, "P8D",       "Port P8 direction register"),
        # symbols 0x0012 and 0x0013 are unused
        Symbol(0x0014, "TXYCON",    "Timer XY control register"),
        Symbol(0x0015, "P2P3C",     "Port P2P3 control register"),
        Symbol(0x0016, "PULL",      "Pull-up control register"),
        Symbol(0x0017, "WDTCON",    "Watchdog timer control register"),
        Symbol(0x0018, "TB_RB",     "Transmit/Receive buffer register"),
        Symbol(0x0019, "SIO1STS",   "Serial I/O1 status register"),
        Symbol(0x001a, "SIO1CON",   "Serial I/O1 control register"),
        Symbol(0x001b, "UARTCON",   "UART control register"),
        Symbol(0x001c, "BRG",       "Baud rate generator"),
        Symbol(0x001d, "SIO2CON1",  "Serial I/O2 control register 1"),
        Symbol(0x001e, "SIO2CON2",  "Serial I/O2 control register 2"),
        Symbol(0x001f, "SIO2",      "Serial I/O2 register"),
        Symbol(0x0020, "TXL",       "Timer X (low-order)"),
        Symbol(0x0021, "TXH",       "Timer X (high-order)"),
        Symbol(0x0022, "TYL",       "Timer Y (low-order)"),
        Symbol(0x0023, "TYH",       "Timer Y (high-order)"),
        Symbol(0x0024, "T1",        "Timer 1"),
        Symbol(0x0025, "T2",        "Timer 2"),
        Symbol(0x0026, "T3",        "Timer 3"),
        Symbol(0x0027, "TXM",       "Timer X mode register"),
        Symbol(0x0028, "TYM",       "Timer Y mode register"),
        Symbol(0x0029, "T123M",     "Timer 123 mode register"),
        Symbol(0x002a, "RTP",       "Real time port register"),
        Symbol(0x002b, "RTPCON0",   "Real time port control register 0"),
        Symbol(0x002c, "RTPCON1",   "Real time port control register 1"),
        Symbol(0x002d, "RTPCON2",   "Real time port control register 2"),
        Symbol(0x002e, "RTPCON3",   "Real time port control register 3"),
        Symbol(0x002f, "TAL",       "Timer A (low-order)"),
        Symbol(0x0030, "TAH",       "Timer A (high-order)"),
        Symbol(0x0031, "TBL",       "Timer B (low-order)"),
        Symbol(0x0032, "TBH",       "Timer B (high-order)"),
        Symbol(0x0033, "DACON",     "D-A control register"),
        Symbol(0x0034, "ADCON",     "A-D control register"),
        Symbol(0x0035, "AD",        "A-D conversion register"),
        Symbol(0x0036, "DA1",       "D-A1 conversion register"),
        Symbol(0x0037, "DA2",       "D-A2 conversion register"),
        Symbol(0x0038, "DA3",       "D-A3 conversion register"),
        Symbol(0x0039, "DA4",       "D-A4 conversion register"),
        Symbol(0x003a, "INTEDGE",   "Interrupt edge selection register"),
        Symbol(0x003b, "CPUM",      "CPU mode register"),
        Symbol(0x003c, "IREQ1",     "Interrupt request register 1"),
        Symbol(0x003d, "IREQ2",     "Interrupt request register 2"),
        Symbol(0x003e, "ICON1",     "Interrupt control register 1"),
        Symbol(0x003f, "ICON2",     "Interrupt control register 2"),

        # vectors
        Symbol(0xfffc, "RESET",     "Reset vector"),
        Symbol(0xfffa, "INT_FFFA",  "INT0"),
        Symbol(0xfff8, "INT_FFF8",  "INT1"),
        Symbol(0xfff6, "INT_FFF6",  "Serial I/O 1 reception"),
        Symbol(0xfff4, "INT_FFF4",  "Serial I/O 2 transmission"),
        Symbol(0xfff2, "INT_FFF2",  "Timer X"),
        Symbol(0xfff0, "INT_FFF0",  "Timer Y"),
        Symbol(0xffee, "INT_FFEE",  "INT3 / Timer 2"),
        Symbol(0xffec, "INT_FFEC",  "INT4 / Timer 3"),
        Symbol(0xffea, "INT_FFEA",  "CNTR0"),
        Symbol(0xffe8, "INT_FFE8",  "CNTR1"),
        Symbol(0xffe6, "INT_FFE6",  "Serial I/O 2"),
        Symbol(0xffe4, "INT_FFE4",  "INT2 / Timer 1"),
        Symbol(0xffe2, "INT_FFE2",  "Timer A"),
        Symbol(0xffe0, "INT_FFE0",  "Timer B"),
        Symbol(0xffde, "INT_FFDE",  "A-D converter / ADT"),
        Symbol(0xffdc, "INT_BRK",   "BRK instruction interrupt"),
    ]
}
# "50734" (e.g. M50734)
# Source: https://archive.org/details/bitsavers_mitsubishiishiSingleChip8BitMicrocomputers_54200624
Devices["50734"] = {"vector_table":
    [ # Interrupt vector table - "50734 Group"
        0xfff4, # TX, CNTR, or BRK
        0xfff6, # HE or VE
        0xfff8, # Timer1, Timer2, or Timer3
        0xfffa, # RI or INT1
        0xfffc, # INT2
        0xfffe, # RESET
    ],
    "symbol_table":
    [ # Symbol Table - "50734 Group"
        # I/O
        Symbol(0x00da, "TXL",       "Timer X (lower byte)"),
        Symbol(0x00db, "TXH",       "Timer X (higher byte)"),
        Symbol(0x00dc, "PRE1",      "Prescaler 1"),
        Symbol(0x00dd, "T1",        "Timer 1"),
        Symbol(0x00de, "PRE2",      "Prescaler 2"),
        Symbol(0x00df, "T2",        "Timer 2"),
        Symbol(0x00e0, "PRE3",      "Prescaler 3"),
        Symbol(0x00e1, "T3",        "Timer 3"),
        Symbol(0x00e2, "HCNT",      "Horizontal counter"),
        Symbol(0x00e3, "VCNT",      "Vertical counter"),
        Symbol(0x00e4, "TSR",       "Transmit shift register"),
        Symbol(0x00e5, "RBR",       "Receive buffer register"),
        Symbol(0x00e6, "UCON",      "UART control register"),
        Symbol(0x00e7, "USR",       "UART status register"),
        Symbol(0x00e8, "SIO",       "Serial I/O register"),
        Symbol(0x00e9, "ADCON",     "A-D control register"),
        Symbol(0x00ea, "ADR",       "A-D register"),
        Symbol(0x00eb, "P4IN",      "Port P4 input"),
        Symbol(0x00ec, "PHASECNT",  "Vertical + Horizontal phase counter"),
        Symbol(0x00ed, "P2P3FUNC",  "Port P2 P3 function register"),
        Symbol(0x00ee, "P3",        "Port P3"),
        Symbol(0x00ef, "P3DIR",     "Port P3 directional register"),
        Symbol(0x00f0, "P2",        "Port P2"),
        Symbol(0x00f1, "P2DIR",     "Port P2 directional register"),
        Symbol(0x00f2, "P1IN",      "Port P1 latch input"),
        Symbol(0x00f3, "P1",        "Port P1"),
        Symbol(0x00f4, "P1DIR",     "Port P1 directional register"),
        Symbol(0x00f5, "P0FUNC",    "Port P0 function register"),
        Symbol(0x00f6, "P0",        "Port P0"),
        Symbol(0x00f7, "P0DIR",     "Port P0 directional register"),
        Symbol(0x00f8, "SMCONH",    "Stepper motor control register H"),
        Symbol(0x00f9, "SMCONV",    "Stepper motor control register V"),
        Symbol(0x00fa, "STBT",      "Strobe timer (Timer S)"),
        Symbol(0x00fb, "BRGTB",     "Baud rate generator (Timer B)"),
        Symbol(0x00fc, "WDT",       "Watchdog timer (Timer W)"),
        Symbol(0x00fd, "ICON3",     "Interrupt control register 3"),
        Symbol(0x00fe, "ICON2",     "Interrupt control register 2"),
        Symbol(0x00ff, "ICON1",     "Interrupt control register 1"),

        # vectors
        Symbol(0xfffe, "RESET",                 "Reset vector"),
        Symbol(0xfffc, "INT_FFFC_INT2",         "INT2 (External interrupt 2)"),
        Symbol(0xfffa, "INT_FFFA_RI_INT1",      "RI or INT1"),
        Symbol(0xfff8, "INT_FFF8_T1T2T3",       "Timer1, Timer2, or Timer3"),
        Symbol(0xfff6, "INT_FFF6_HEVE",         "HE or VE"),
        Symbol(0xfff4, "INT_FFF4_TXCNTRBRK",    "TX, CNTR, or BRK"),

    ]
}
# Add an "alias" for M50734
Devices["M50734"] = Devices["50734"]
