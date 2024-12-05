import struct
import time

class Registers:
    def __init__(self):
        self.registers = [0] * 32

    def __getitem__(self, key):
        if key == 0:
            return 0
        return self.registers[key]
    def __setitem__(self, key, value):
        if key == 0:
            return
        self.registers[key] = value

    def __repr__(self):
        return f'{self.registers}'

class CPU:
    def __init__(self, debug: bool = False):
        self.registers = Registers()
        self.memory = [0] * 0x300040
        self.pc = 0x40
        self.instruction = 0
        self.debug = debug
        self.decode_table = {
            0b000000: self.add,
            0b000001: self.sub,
            0b000010: self.addi,
            0b000011: self.subi,
            0b000100: self.lui,
            0b000101: self.show,
            0b000110: self.stall,
            0b000111: self.ld,
            0b001000: self.sr,
            0b001001: self.jmp,
            0b001010: self.jmpeq,
            0b001011: self.hlt,
        }
        self.debug_table = {
            0b000000: 'add',
            0b000001: 'sub',
            0b000010: 'addi',
            0b000011: 'subi',
            0b000100: 'lui',
            0b000101: 'show',
            0b000110: 'stall',
            0b000111: 'ld',
            0b001000: 'sr',
            0b001001: 'jmp',
            0b001010: 'jmpeq',
            0b001011: 'hlt',
        }

    def load_data_at(self, programfile: str, addr: int, small: bool = False):
        with open(programfile, 'rb') as f:
            while True:
                chunk = f.read(4)
                if not chunk:
                    break
                word = struct.unpack('>I', chunk)[0]
                if small:
                    word = struct.unpack('<I', chunk)[0]
                self.memory[addr] = word
                addr += 1
        return addr

    def cycle(self):
        self.instruction = self.memory[self.pc]
        opcode = self.instruction >> 26
        if self.debug:
            self.debugprint(opcode)
        self.pc += 1
        self.decode_table[opcode]()

    def debugprint(self, opcode: int):
        print(f'opcode: {self.debug_table[opcode]}, instruction: {self.instruction:032b}')


    def add(self):
        r1 = (self.instruction >> 21) & 0b11111
        r2 = (self.instruction >> 16) & 0b11111
        r3 = (self.instruction >> 11) & 0b11111
        self.registers[r1] = self.registers[r2] + self.registers[r3]

    def sub(self):
        r1 = (self.instruction >> 21) & 0b11111
        r2 = (self.instruction >> 16) & 0b11111
        r3 = (self.instruction >> 11) & 0b11111
        self.registers[r1] = self.registers[r2] - self.registers[r3]

    def addi(self):
        r1 = (self.instruction >> 21) & 0b11111
        imm = (self.instruction >> 5) & 0xffff
        self.registers[r1] = self.registers[r1]+imm

    def subi(self):
        r1 = (self.instruction >> 21) & 0b11111
        imm = (self.instruction >> 5) & 0xffff
        self.registers[r1] = self.registers[r1]-imm

    def lui(self):
        r1 = (self.instruction >> 21) & 0b11111
        imm = (self.instruction >> 5) & 0xffff
        self.registers[r1] = imm << 16

    def show(self):
        data = self.memory[0:64]
        frame = ''
        for i in range(0, 64, 2):
            chunk = data[i] | data[i+1] << 32
            for j in range(64):
                if chunk & (1 << j) != 0:
                    frame += '  '
                else:
                    frame += '██'
            frame += '\n'
        print(frame)

    def stall(self):
        sleep_time = (self.instruction >> 10) & 0xffff
        sleep_time /= 1000
        time.sleep(sleep_time)

    def ld(self):
        r1 = (self.instruction >> 21) & 0b11111
        r2 = (self.instruction >> 16) & 0b11111
        self.registers[r1] = self.memory[self.registers[r2]]

    def sr(self):
        r1 = (self.instruction >> 21) & 0b11111
        r2 = (self.instruction >> 16) & 0b11111
        self.memory[self.registers[r2]] = self.registers[r1]

    def jmp(self):
        r1 = (self.instruction >> 21) & 0b11111
        self.pc = self.registers[r1]

    def jmpeq(self):
        r1 = (self.instruction >> 21) & 0b11111
        r2 = (self.instruction >> 16) & 0b11111
        r3 = (self.instruction >> 11) & 0b11111
        if self.registers[r1] == self.registers[r2]:
            self.pc = self.registers[r3]

    def hlt(self):
        print("halt")
        exit(0)

