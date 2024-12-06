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

instr:
li r1, 3
li r2, 4
li r31, instr
li r30, jump
li r29, jump_eq
add r3, r1, r2
addi r3, 4
subi r3, 4
lui r4, 1
stall 1000
ld r5, [r31]
sr r1, [r31]
jmp r30
add r1, r1, r1
add r1, r1, r1
jump:
jmpeq r1, r2, r30
jmpeq r1, r1, r29
add r1, r1, r1
add r1, r1, r1
jump_eq:
hlt
