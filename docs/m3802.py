# Special Function Registers for 3802 Group
# Source: https://www.renesas.com/en/document/dst/3802-group-datasheet

sfrs = {
    0x0000: ('P0',       'Port P0'),
    0x0001: ('P0D',      'Port P0 direction register'),
    0x0002: ('P1',       'Port P1'),
    0x0003: ('P1D',      'Port P1 direction register'),
    0x0004: ('P2',       'Port P2'),
    0x0005: ('P2D',      'Port P2 direction register'),
    0x0006: ('P3',       'Port P3'),
    0x0007: ('P3D',      'Port P3 direction register'),
    0x0008: ('P4',       'Port P4'),
    0x0009: ('P4D',      'Port P4 direction register'),
    0x000a: ('P5',       'Port P5'),
    0x000b: ('P5D',      'Port P5 direction register'),
    0x000c: ('P6',       'Port P6'),
    0x000d: ('P6D',      'Port P6 direction register'),
    # SFRs 0x000e - 0x0017 are unused
    0x0018: ('TB_RB',    'Transmit/Receive buffer register'),
    0x0019: ('SIO1STS',  'Serial I/O1 status register'),
    0x001a: ('SIO1CON',  'Serial I/O1 control register'),
    0x001b: ('UARTCON',  'UART control register'),
    0x001c: ('BRG',      'Baud rate generator'),
    0x001d: ('SIO2CON',  'Serial I/O2 control register'),
    # SFR 0x001e is unused
    0x001f: ('SIO2',     'Serial I/O2 register'),
    0x0020: ('PRE12',    'Prescaler 12'),
    0x0021: ('T1',       'Timer 1'),
    0x0022: ('T2',       'Timer 2'),
    0x0023: ('TM',       'Timer XY mode register'),
    0x0024: ('PREX',     'Prescaler X'),
    0x0025: ('TX',       'Timer X'),
    0x0026: ('PREY',     'Prescaler Y'),
    0x0027: ('TY',       'Timer Y'),
    # SFRs 0x0028 - 0x002a are unused
    0x002b: ('PWMCON',   'PWM control register'),
    0x002c: ('PREPWM',   'PWM prescaler'),
    0x002d: ('PWM',      'PWM register'),
    # SFRs 0x002e - 0x0033 are unused
    0x0034: ('ADCON',    'AD/DA control register'),
    0x0035: ('AD',       'A-D conversion register'),
    0x0036: ('DA1',      'D-A1 conversion register'),
    0x0037: ('DA2',      'D-A2 conversion register'),
    # SFRs 0x0038 - 0x0039 are unused
    0x003a: ('INTEDGE',  'Interrupt edge selection register'),
    0x003b: ('CPUM',     'CPU mode register'),
    0x003c: ('IREQ1',    'Interrupt request register 1'),
    0x003d: ('IREQ2',    'Interrupt request register 2'),
    0x003e: ('ICON1',    'Interrupt control register 1'),
    0x003f: ('ICON2',    'Interrupt control register 2'),
}

for address, (name, desc) in sfrs.items():
    print('%04x: %s \t;%s' % (address, name, desc))
    # print('%04x: (\'%s\', \t\'%s\'),' % (address, name, desc))
