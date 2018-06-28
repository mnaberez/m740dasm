
    .area CODE1 (ABS)
    .org 0x8000

    ;Addressing Modes

    adc #0xA5           ;69 A5      Immediate
    rol A               ;2A         Accumulator
    adc 0xaa            ;65 AA      Zero Page
    adc 0xaa,x          ;75 AA      Zero Page X
    ldx 0xaa,y          ;B6 AA      Zero Page Y
    adc 0xaabb          ;6D BB AA   Absolute
    adc 0xaabb,x        ;7D BB AA   Absolute X
    adc 0xaabb,y        ;79 BB AA   Absolute Y
    clc                 ;18         Implied
label1:
    bcc label1          ;90 xx      Relative
    adc [0xaa,x]        ;61 1E      Indirect X
    adc [0xaa],y        ;71 1E      Indirect Y
    jmp [0xaabb]        ;6C 00 14   Indirect Absolute
    jmp [0xaa]          ;B2 AA      Zero Page Indirect
    ;jmp \0xFFC0         ;22 C0      Special Page         TODO assembly error
    clb 5,0xaa          ;BF 44      Zero Page Bit
    clb 5,A             ;BB         Accumulator Bit
label2:
    bbc 5,A,label2      ;B3 xx      Accumulator Bit Relative
label3:
    bbc 5,0xaa,label3   ;B7 04 xx   Zero Page Bit Relative
    ldm #0xaa,0xbb      ;3C TODO    Zero Page Immediate

    ;Instructions

    brk                 ;00         Implied
    ora [0x1E,x]        ;01 1E      Indirect X
    jsr [0x45]          ;02 45      Zero Page Indirect
label4:
    bbs 0,a,label4      ;03 FE      Accumulator Bit Relative
    .byte 0x04          ;04 00      Illegal
    ora 0x45            ;05 45      Zero Page
    asl 0x45            ;06 45      Zero Page
label5:
    bbs 0,0xaa,label5   ;07 45      Zero Page Bit Relative
    php                 ;08         Implied
    ora #0xaa           ;09         Immediate
    asl a               ;0a         Implied
    seb 0,a             ;0b         Accumulator Bit Relative
    .byte 0x0c          ;0c         Illegal
    ora 0xaabb          ;0d         Absolute
    asl 0xaabb          ;0e         Absolute
    seb 0,0xaa          ;0f         Zero Page Bit
label6:
    bpl label6          ;10         Relative
    ora [0x1E],y        ;11         Indirect Y
    clt                 ;12         Implied
label7:
    bbc 0,a,label7      ;13         Accumulator Bit Relative
    .byte 0x14          ;14         Illegal
    ora 0xaa,x          ;15         Zero Page X
    asl 0xaa,x          ;16         Zero Page X
label8:
    bbc 0,a,label8      ;17         Accumulator Bit Relative
    clc                 ;18         Implied
    ora 0xaabb,y        ;19         Absolute Y
    dec a               ;1a         Implied
    clb 0,a             ;1b         Accumulator Bit
    .byte 0x1c          ;1c         Illegal
    ora 0xaabb,x        ;1d         Absolute X
    asl 0xaabb,x        ;1e         Absolute X
    clb 0,0xaa          ;1f         Zero Page Bit
    jsr 0xaabb          ;20         Absolute
    and 0xaa,x          ;21         Indirect X
    .byte 0x22          ;22         Special Page        TODO fix assembly
label9:
    bbs 1,a,label9      ;23         Zero Page Bit Relative
    bit 0xaa            ;24         Zero Page
    and 0xaa            ;25         Zero Page
    rol 0xaa            ;26         Zero Page
label10:
    bbs 1,0xaa,label10  ;27         Zero Page Bit Relative
    plp                 ;28         Implied
    and #0xaa           ;29         Immediate
    rol a               ;2a         Implied
    seb 1,a             ;2b         Accumulator Bit
    bit 0xaabb          ;2c         Absolute
    and 0xaabb          ;2d         Absolute
    rol 0xaabb          ;2e         Absolute
    seb 1,0xa           ;2f         Zero Page Bit
label11:
    bmi label11         ;30         Relative
    and [0xaa],y        ;31         Indirect Y
    set                 ;32         Implied
label12:
    bbc 1,a,label12     ;33         Accumulator Bit Relative
    .byte 0x34          ;34         Illegal
    and 0xaa,x          ;35         Zero Page X
    rol 0xaa,x          ;36         Zero Page X
label13:
    bbc 1,0xaa,label13  ;37         Zero Page Bit Relative
    sec                 ;38         Implied
    and 0xaabb,y        ;39         Absolute Y
    inc a               ;3a         Implied
    clb 1,a             ;3b         Accumulator Bit
    ldm #0xaa,0xbb      ;3c         Zero Page Immediate
    and 0xaabb,x        ;3d         Absolute X
    rol 0xaabb,x        ;3e         Absolute X
    clb 1,0xaa          ;3f         Zero Page Bit
    rti                 ;40         Implied
    eor [0xaa,x]        ;41         Indirect X
    stp                 ;42         Implied
label14:
    bbs 2,a,label14     ;43         Accumulator Bit
    com 0xaa            ;44         Zero Page
    eor 0xaa            ;45         Zero Page
    lsr 0xaa            ;46         Zero Page
label15:
    bbs 2,0xaa,label15  ;47         Zero Page Bit Relative
    pha                 ;48         Implied
    eor #0xaa           ;49         Immediate
    lsr a               ;4a         Implied
    seb 2,a             ;4b         Accumulator Bit
    jmp 0xaabb          ;4c         Absolute
    eor 0xaabb          ;4d         Absolute
    lsr 0xaabb          ;4e         Absolute
    seb 2,0xaa          ;4f         Zero Page Bit
label16:
    bvc label16         ;50         Relative
    eor [0xaa],y        ;51         Indirect Y
    .byte 0x52          ;52         Illegal
label17:
    bbc 2,a,label17     ;53         Accumulator Bit Relative
    .byte 0x54          ;54         Illegal
    eor 0xaa,x          ;55         Zero Page X
    lsr 0xaa,x          ;56         Zero Page X
label18:
    bbc 2,0xaa,label18  ;57         Zero Page Bit Relative
    cli                 ;58         Inherent
    eor 0xaabb,y        ;59         Absolute Y
    .byte 0x5a          ;5a         Illegal
    clb 2,a             ;5b         Accumulator Bit
    .byte 0x5c          ;5c         Illegal
    eor 0xaabb,x        ;5d         Absolute X
    lsr 0xaabb,x        ;5e         Absolute X
    clb 2,0xaa          ;5f         Zero Page Bit
    rts                 ;60         Implied
    adc [0xaa,x]        ;61         Indirect X
    mul 0xaa,x          ;62         Zero Page X
label19:
    bbs 3,a,label19     ;63         Accumulator Bit Relative
    tst 0xaa            ;64         Zero Page
    adc 0xaa            ;65         Zero Page
    ror 0xaa            ;66         Zero Page
label20:
    bbs 3,0xaa,label20  ;67         Zero Page Bit Relative
    pla                 ;68         Implied
    adc #0xaa           ;69         Immediate
    ror a               ;6a         Implied
    seb 3,a             ;6b         Accumulator Bit
    jmp [0xaabb]        ;6c         Indirect Absolute
    adc 0xaabb          ;6d         Absolute
    ror 0xaabb          ;6e         Absolute
    seb 3,0xaa          ;6f         Zero Page Bit
label21:
    bvs label21         ;70         Relative
    adc [0xaa],y        ;71         Indirect Y
    .byte 0x72          ;72         Illegal
label22:
    bbc 3,a,label22     ;73         Accumulator Bit Relative
    .byte 0x74          ;74         Illegal
    adc 0xaa,x          ;75         Zero Page X
    ror 0xaa,x          ;76         Zero Page X
label23:
    bbc 3,0xaa,label23  ;77         Zero Page Bit Relative
    sei                 ;78         Implied
    adc 0xaabb,y        ;79         Absolute Y
    .byte 0x7a          ;7a         Illegal
    clb 3,a             ;7b         Accumulator Bit
    .byte 0x7c          ;7c         Illegal
    adc 0xaabb,x        ;7d         Absolute X
    ror 0xaabb,x        ;7e         Absolute X
    clb 3,0xaa          ;7f         Zero Page Bit
label24:
    bra label24         ;80         Relative
    sta [0xaa,x]        ;81         Indirect X
    rrf 0xaa            ;82         Zero Page
label25:
    bbs 4,a,label25     ;83         Accumulator Bit Relative
    sty 0xaa            ;84         Zero Page
    sta 0xaa            ;85         Zero Page
    stx 0xaa            ;86         Zero Page
label26:
    bbs 4,0xaa,label26  ;87         Zero Page Bit Relative
    dey                 ;88         Implied
    .byte 0x89          ;89         Illegal
    txa                 ;8a         Implied
    seb 4,a             ;8b         Accumulator Bit
    sty 0xaabb          ;8c         Accumulator
    sta 0xaabb          ;8d         Accumulator
    stx 0xaabb          ;8e         Accumulator
    seb 4,0xaa          ;8f         Zero Page Bit
label27:
    bcc label27         ;90         Relative
    sta [0xaa],y        ;91         Indirect Y
    .byte 0x92          ;92         Illegal
label28:
    bbc 4,a,label28     ;93         Accumulator Bit Relative
    sty 0xaa,x          ;94         Zero Page X
    sta 0xaa,x          ;95         Zero Page X
    stx 0xaa,y          ;96         Zero Page Y
label29:
    bbc 4,0xaa,label29  ;97         Zero Page Bit Relative
    tya                 ;98         Implied
    sta 0xaabb,y        ;99         Absolute Y
    txs                 ;9a         Implied
    clb 4,a             ;9b         Accumulator Bit
    .byte 0x9c          ;9c         Illegal
    sta 0xaabb,x        ;9d         Absolute X
    .byte 0x9e          ;9e         Illegal
    clb 4,0xaa          ;9f         Zero Page Bit
    ldy #0xaa           ;a0         Immediate
    lda [0xaa,x]        ;a1         Indirect X
    ldx #0xaa           ;a2         Immediate
label30:
    bbs 5,a,label30     ;a3         Accumulator Bit Relative
    ldy 0xaa            ;a4         Zero Page
    lda 0xaa            ;a5         Zero Page
    ldx 0xaa            ;a6         Zero Page
label31:
    bbs 5,0xaa,label31  ;a7         Accumulator Bit Relative
    tay                 ;a8         Implied
    lda #0xaa           ;a9         Immediate
    tax                 ;aa         Implied
    seb 5,a             ;ab         Accumulator Bit
    ldy 0xaabb          ;ac         Absolute
    lda 0xaabb          ;ad         Absolute
    ldx 0xaabb          ;ae         Absolute
    seb 5,0xaa          ;af         Zero Page Bit
label32:
    bcs label32         ;b0         Relative
    lda [0xaa],y        ;b1         Indirect Y
    jmp [0xaa]          ;b2         Zero Page Indirect
label33:
    bbc 5,a,label33     ;b3         Accumulator Bit Relative
    ldy 0xaa,x          ;b4         Zero Page X
    lda 0xaa,x          ;b5         Zero Page X
    lda 0xaa,y          ;b6         Zero Page Y
label34:
    bbc 5,0xaa,label34  ;b7         Zero Page Bit Relative
    clv                 ;b8         Implied
    lda 0xaabb,y        ;b9         Absolute Y
    tsx                 ;ba         Implied
    clb 5,a             ;bb         Accumulator Bit
    ldy 0xaabb,x        ;bc         Absolute X
    lda 0xaabb,x        ;bd         Absolute X
    ldx 0xaabb,y        ;be         Absolute Y
    clb 5,0xaa          ;bf         Zero Page Bit
    cpy #0xaa           ;c0         Immediate
    cmp [0xaa,x]        ;c1         Indirect X
    wit                 ;c2         Implied
label35:
    bbs 6,a,label35     ;c3         Accumulator Bit Relative
    cpy 0xaa            ;c4         Zero Page
    cmp 0xaa            ;c5         Zero Page
    dec 0xaa            ;c6         Zero Page
label36:
    bbs 6,0xaa,label36  ;c7         Zero Page Bit Relative
    iny                 ;c8         Implied
    cmp #0xaa           ;c9         Immediate
    dex                 ;ca         Implied
    seb 6,a             ;cb         Accumulator Bit
    cpy 0xaabb          ;cc         Absolute
    cmp 0xaabb          ;cd         Absolute
    dec 0xaabb          ;ce         Absolute
    seb 6,0xaa          ;cf         Zero Page Bit
label37:
    bne label37         ;d0         Relative
    cmp [0xaa],y        ;d1         Indirect Y
    .byte 0xd2          ;d2         Illegal
label38:
    bbc 6,a,label38     ;d3         Accumulator Bit Relative
    .byte 0xd4          ;d4         Illegal
    cmp 0xaa,x          ;d5         Zero Page X
    dec 0xaa,x          ;d6         Zero Page X
label39:
    bbc 6,0xaa,label39  ;d7         Zero Page Bit Relative
    cld                 ;d8         Implied
    cmp 0xaabb,y        ;d9         Absolute Y
    .byte 0xda          ;da         Illegal
    clb 6,a             ;db         Accumulator Bit
    .byte 0xdc          ;dc         Illegal
    cmp 0xaabb,x        ;dd         Absolute X
    dec 0xaabb,x        ;de         Absolute X
    clb 6,0xaa          ;df         Zero Page Bit
    cpx #0xaa           ;e0         Immediate
    sbc [0xaa,x]        ;e1         Indirect X
    div 0xaa,x          ;e2         Zero Page X
label40:
    bbs 7,a,label40     ;e3         Accumulator Bit Relative
    cpx 0xaa            ;e4         Zero Page
    sbc 0xaa            ;e5         Zero Page
    inc 0xaa            ;e6         Zero Page
label41:
    bbs 7,a,label41     ;e7         Accumulator Bit Relative
    cpx 0xaa            ;e8         Zero Page
    sbc 0xaa            ;e9         Zero Page
    nop                 ;ea         Implied
    seb 7,a             ;eb         Accumulator Bit
    cpx 0xaabb          ;ec         Absolute
    sbc 0xaabb          ;ed         Absolute
    inc 0xaabb          ;ee         Absolute
    seb 7,0xaa          ;ef         Zero Page Bit
label42:
    beq label42         ;f0         Relative
    sbc [0xaa],y        ;f1         Indirect Y
    .byte 0xf2          ;f2         Illegal
label43:
    bbc 7,a,label43     ;f3         Accumulator Bit Relative
    .byte 0xf4          ;f4         Illegal
    sbc 0xaa,x          ;f5         Zero Page X
    inc 0xaa,x          ;f6         Zero Page X
label44:
    bbc 7,0xaa,label44  ;f7         Zero Page Bit Relative
    sed                 ;f8         Implied
    sbc 0xaabb,y        ;f9         Absolute Y
    .byte 0xfa          ;fa         Illegal
    clb 7,a             ;fb         Accumulator Bit
    .byte 0xfc          ;fc         Illegal
    sbc 0xaabb,x        ;fd         Absolute X
    inc 0xaabb,x        ;fe         Absolute X
    clb 7,0xaa          ;ff         Zero Page Bit
