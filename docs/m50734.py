# Special Function Registers for 50734 Group
# Source: https://archive.org/details/bitsavers_mitsubishiishiSingleChip8BitMicrocomputers_54200624

sfrs = {

    0x00da: ('TXL',       'Timer X (lower byte)'),
    0x00db: ('TXH',       'Timer X (higher byte)'),
    0x00dc: ('PRE1',      'Prescaler 1'),
    0x00dd: ('T1',        'Timer 1'),
    0x00de: ('PRE2',      'Prescaler 2'),
    0x00df: ('T2',        'Timer 2'),
    0x00e0: ('PRE3',      'Prescaler 3'),
    0x00e1: ('T3',        'Timer 3'),
    0x00e2: ('HCNT',      'Horizontal counter'),
    0x00e3: ('VCNT',      'Vertical counter'),
    0x00e4: ('TSR',       'Transmit shift register'),
    0x00e5: ('RBR',       'Receive buffer register'),
    0x00e6: ('UCON',      'UART control register'),
    0x00e7: ('USR',       'UART status register'),
    0x00e8: ('SIO',       'Serial I/O register'),
    0x00e9: ('ADCON',     'A-D control register'),
    0x00ea: ('ADR',       'A-D register'),
    0x00eb: ('P4IN',      'Port P4 input'),
    0x00ec: ('PHASECNT',  'Vertical + Horizontal phase counter'),
    0x00ed: ('P2P3FUNC',  'Port P2 P3 function register'),
    0x00ee: ('P3',        'Port P3'),
    0x00ef: ('P3DIR',     'Port P3 directional register'),
    0x00f0: ('P2',        'Port P2'),
    0x00f1: ('P2DIR',     'Port P2 directional register'),
    0x00f2: ('P1IN',      'Port P1 latch input'),
    0x00f3: ('P1',        'Port P1'),
    0x00f4: ('P1DIR',     'Port P1 directional register'),
    0x00f5: ('P0FUNC',    'Port P0 function register'),
    0x00f6: ('P0',        'Port P0'),
    0x00f7: ('P0DIR',     'Port P0 directional register'),
    0x00f8: ('SMCONH',    'Stepper motor control register H'),
    0x00f9: ('SMCONV',    'Stepper motor control register V'),
    0x00fa: ('STBT',      'Strobe timer (Timer S)'),
    0x00fb: ('BRGTB',     'Baud rate generator (Timer B)'),
    0x00fc: ('WDT',       'Watchdog timer (Timer W)'),
    0x00fd: ('ICON3',     'Interrupt control register 3'),
    0x00fe: ('ICON2',     'Interrupt control register 2'),
    0x00ff: ('ICON1',     'Interrupt control register 1'),

}

for address, (name, desc) in sfrs.items():
    print("%04x: %s \t;%s" % (address, name, desc))
    # print("%04x: (\"%s\", \t\"%s\")," % (address, name, desc))
