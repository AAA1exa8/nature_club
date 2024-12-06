prvních 12 instrukcí jen načítá
v 2. a 3. registru by měli být hodnoty 3 a 4 respektive
do 4. registru by se mělo sečíct 2 a 3 (v registru by měla být hodnota 7)
k 4. registru by se mělo přičíst 4 (v registru by měla být hodnota 11)
od 4. registru by se mělo odečíst 4 (v registru by měla být hodnota 7)
do 5. registru by se měla načíst hodnota z paměti na adrese první instrukce
do adresy v registru 31 by se měl uložit obsah registru 1 (tedy 3)
další dvě instrukce add by se měli přeskočit (v druhém registru by měla být hodnota 3)
poté by se měli spustit dvě instrukce jmpeq jen jedna z nich by se měla spustit
procesor by se měl zastavit

```asm
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
```
