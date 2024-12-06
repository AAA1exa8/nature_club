#bankdef program {
    #bits 32
    #addr 0x000040
    #size 0x300000
    #outp 0
}

#ruledef {
    add r{r1: u5}, r{r2: u5}, r{r3: u5}   => 0b000000 @ r1 @ r2 @ r3 @ 0b00000000000 
    sub r{r1: u5}, r{r2: u5}, r{r3: u5}   => 0b000001 @ r1 @ r2 @ r3 @ 0b00000000000 
    addi r{r1: u5}, {imm: u16}            => 0b000010 @ r1 @ imm @ 0b00000
    subi r{r1: u5}, {imm: u16}            => 0b000011 @ r1 @ imm @ 0b00000
    lui r{r1: u5}, {imm: u16}             => 0b000100 @ r1 @ imm @ 0b00000
    show                                  => 0b000101 @ 0b00000000000000000000000000
    stall {imm: u16}                      => 0b000110 @ imm @ 0b0000000000
    ld r{r1: u5}, [r{r2: u5}]             => 0b000111 @ r1 @ r2 @ 0b0000000000000000
    sr r{r1: u5}, [r{r2: u5}]             => 0b001000 @ r1 @ r2 @ 0b0000000000000000
    jmp r{r1: u5}                         => 0b001001 @ r1 @ 0b000000000000000000000
    jmpeq r{r1: u5}, r{r2: u5}, r{r3: u5} => 0b001010 @ r1 @ r2 @ r3 @ 0b00000000000
    hlt                                   => 0b001011 @ 0b00000000000000000000000000
}

#ruledef {
    mov r{r1: u5}, r{r2: u5} => asm { add r{r1}, r{r2}, r0 }
    li r{r1: u5}, {immm: u32} => asm { mov r{r1}, r0 } @ asm { lui r{r1}, {immm}[31:16] } @ asm { addi r{r1}, {immm}[15:0] }
}

li r1, data
li r2, 64
li r3, 0
li r10, 0
li r11, frame
li r12, loop
loop:
    ld r4, [r1]
    sr r4, [r3]
    addi r1, 1
    addi r3, 1
    subi r2, 1
    jmpeq r2, r10, r11
    jmp r12
frame:
    stall 33
    show
    li r13, 420714
    li r14, halt
    li r2, 64
    li r3, 0
    jmpeq r13, r1, r14 
    jmp r12
halt:
    hlt

data:
