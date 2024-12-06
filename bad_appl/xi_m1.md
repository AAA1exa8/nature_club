# Dokumentace XI_M1 Fiktivního Procesoru

Shrnutí technické specifikace

- 12 instrukcí
- Šířka slova je 32 bitů
- Program začíná na adrese 0x40
- K procesoru je připojený jeden 64x32 pixelů display

# Procesor

Procesor XI_M1 (dále jen XI) má 32 general purpouse registrů r0-r31. Registr r0 vždy vrací při čtení 0 a zápis vždy zahodí.

## Pamněť

Procesor má operační pamněť 12MB. To znamená 0x300000 pamněťových buňek po 32 bitech.
Program se načítá na adresu 0x40 to je i adresa na kterou je inicializovaný program counter.
Program má big endianess.

# Instrukce

Procesor má 12 instrukcí 5 aritmetických, 3 na Input/Output, 2 instrukce na skoky a 2 instrukce na ovládání procesoru.

## Enkódování instruckí

XI má 6 různých enkódování instruckí S, D, T, I, O a E.
6 nejvyšších bitů v instrukci je vždy opcode neboli operation code.

```
           bit 26                        bit 0
           |                             |
    0b000000 00 00000000 00000000 00000000
      |
      opcode
```

### S Enkódování

S, Single enkódování enkóduje jeden registr který se nachází hned po opcode.

```
        bit 26   bit 21                  bit 0
           |     |                       |
    0b000000 00000 00000 00000000 00000000
      |      |
      opcode r1
```

### D Enkódování

D, Double enkódovánhí enkóduje dva registry které se nacházejí hned po opcode.

```
        bit 26  bit 21 bit 16           bit 0
           |     |     |                |
    0b000000 00000 00000 00000000 00000000
      |      |         |
      opcode r1        r2
```

### T Enkódování

T, Triple enkódovánhí enkóduje tři registry které se nacházejí hned po opcode.

```
        bit 26 bit 21 bit 16 bit 11           bit 0
   E        |     |     |     |           |
    0b000000 00000 00000 00000 000 00000000
      |      |         |     |
      opcode r1        r2    r3
```

### I Enkódování

I, Immediate Enkódování enkóduje jeden register a jeden 16 bit immediate okamžitě po opcode.

```
        bit 26   bit 21           bit 5  bit 0
           |     |                |      |
    0b000000 00000 0000000000000000  00000
      |      |                    |
      opcode r1                   imm
```

### O Enkódování

O, Only Immediate Enkódování enkóduje jeden 16 bit immediate okamžitě po opcode.

```
        bit 26             bit 10  bit 0
           |                |      |
    0b000000 0000000000000000 00 00000000
      |                     |
      opcode                imm
```

### E Enkódování

E, Empty enkdódování je pouze opcode

```
           bit 26                        bit 0
           |                             |
    0b000000 00 00000000 00000000 00000000
      |
      opcode
```

## Aritmetické instrukce

### `add` a `sub` Instrukce

`add` a `sub` instrukce jsou `T` enkódováné instrukce.
`add` sečte hodnoty v registrech r2 a r3 a výsledek uloží do r1.
`sub` odečte hodnoty v registrech r2 a r3 a výsledek uloží do r1.

### `addi` a `subi` Instrukce

`addi` a `subi` instrukce jsou `I` enkódováné instrukce.
`addi` sečte hodnotu v registru r2 a immediate hodnotu a výsledek uloží do r1.
`subi` odečte hodnotu v registru r2 a immediate hodnotu a výsledek uloží do r1.

### `lui` Instrukce

`lui` instrukce je `I` enkódováná instrukce.
`lui` načte immediate hodnotu do horních 16 bitů registru r1.

## Input/Output instrukce

### `ld` a `sr` Instrukce

`ld` a `sr` instrukce jsou `D` enkódováné instrukce.
`ld` načte hodnotu z adresy v registru r2 a uloží ji do registru r1.
`sr` uloží hodnotu z registru r1 do adresy v registru r2.

### `show` Instrukce

`show` instrukce je `E` enkódováná instrukce.
Show zobrazí na display kontent adres 0x0 až 0x39.
Každý bit čísla endkóduje černou (0) nebo bílou (1).
Jeden řádek je tedy 64 bitů (data z dvou buňek).
Nultý bit enkóduje první pixel atd...

## Skokové instrukce

### `jmp` a `jmpeq` Instrukce

`jmp` je `S` enkódováná instrukce.
`jmp` skočí na adresu v registru r1.
Další instrukce se načte z adresy na kterou skočil.

`jmpeq` je `T` enkódováná instrukce.
`jmpeq` skočí na adresu v registru r1 pokud je hodnota v registru r2 rovna hodnotě v registru r3.
Další instrukce se načte z adresy na kterou skočil nebo se normálně spustí další instrukce.

## Ovládání procesoru

### `stall` a `hlt` Instrukce

`stall` je `O` enkódováná instrukce.
`stall` zastaví procesor na dalších X ms kde X je immediate hodnota.

`hlt` je `E` enkódováná instrukce.
`hlt` zastaví procesor.
