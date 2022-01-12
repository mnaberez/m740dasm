# Special Function Registers for 7451 Group

sfrs = {
    0x00d0: ('P0',      'Port P0'),
    0x00d1: ('P0D',     'Port P0 directional register'),
    0x00d2: ('P1',      'Port P1'),
    0x00d3: ('P1D',     'Port P1 directional register'),
    0x00d4: ('P2',      'Port P2'),
    0x00d5: ('P2D',     'Port P2 directional register'),
    0x00d6: ('P3',      'Port P3'),
    0x00d7: ('P3D',     'Port P3 directional register'),
    0x00d8: ('P4',      'Port P4 / PWM prescaler latch'),
    0x00d9: ('AFD',     'Additional function register'),
    0x00da: ('P5',      'Port P5'),
    0x00db: ('P5D',     'Port P5 direction register'),
    0x00dc: ('P6',      'Port P6'),
    0x00dd: ('P6D',     'Port P6 direction register'),
    0x00de: ('MISRG1',  'Miscellaneous register 1'),
    0x00df: ('MISRG2',  'Miscellaneous register 2'),
    0x00e0: ('DA1',     'D-A1 conversion register'),
    0x00e1: ('DA2',     'D-A2 conversion register'),
    0x00e2: ('AD',      'A-D conversion register'),
    0x00e3: ('ADCNT',   'A-D control register'),
    0x00e4: ('DBB',     'Data bus buffer register'),
    0x00e5: ('DBBSTS',  'Data bus buffer status register'),
    0x00e6: ('RTB',     'Receive/Transmit buffer register'),
    0x00e7: ('SIOSTS',  'Serial I/O status register'),
    0x00e8: ('SIOCON',  'Serial I/O control register'),
    0x00e9: ('UARTCON', 'UART control register'),
    0x00ea: ('BRG',     'Baud rate generator'),
    0x00eb: ('PWMH',    'PWM register (low-order)'),
    0x00ec: ('PWML',    'PWM register (high-order)'),
    0x00ed: ('T1CON',   'Timer 1 control register'),
    0x00ee: ('T2CON',   'Timer 2 control register'),
    0x00ef: ('T3CON',   'Timer 3 control register'),
    0x00f0: ('T1L',     'Timer 1 register (low-order)'),
    0x00f1: ('T1H',     'Timer 1 register (high-order)'),
    0x00f2: ('T1LATL',  'Timer 1 latch (low-order)'),
    0x00f3: ('T1LATH',  'Timer 1 latch (high-order)'),
    0x00f4: ('T2L',     'Timer 2 register (low-order)'),
    0x00f5: ('T2H',     'Timer 2 register (high-order)'),
    0x00f6: ('T2LATL',  'Timer 2 latch (low-order)'),
    0x00f7: ('T2LATH',  'Timer 2 latch (high-order)'),
    0x00f8: ('T3L',     'Timer 3 register (low-order)'),
    0x00f9: ('T3H',     'Timer 3 register (high-order)'),
    0x00fa: ('T3LATL',  'Timer 3 latch (low-order)'),
    0x00fb: ('T3LATH',  'Timer 3 latch (high-order)'),
    0x00fc: ('IREQ1',   'Interrupt request register 1'),
    0x00fd: ('IREQ2',   'Interrupt request register 2'),
    0x00fe: ('ICON1',   'Interrupt control register 1'),
    0x00ff: ('ICON2',   'Interrupt control register 2'),
}

for address, (name, desc) in sfrs.items():
    print("%04x: %s \t;%s" % (address, name, desc))
    # print("%04x: (\"%s\", \t\"%s\")," % (address, name, desc))
