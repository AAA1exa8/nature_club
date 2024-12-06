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
        return

    def debugprint(self, opcode: int):
        print(f'opcode: {self.debug_table[opcode]}, instruction: {
              self.instruction:032b}')

    def add(self):
        return

    def sub(self):
        return

    def addi(self):
        return

    def subi(self):
        return

    def lui(self):
        return

    def show(self):
        data = self.memory[0:64]
        frame = '\n'.join(
            ''.join('  ' if (data[i] << 32 | data[i+1]) &
                    (1 << j) else '██' for j in range(64))
            for i in range(0, 64, 2)
        )
        print(frame)

    def stall(self):
        return

    def ld(self):
        return

    def sr(self):
        return

    def jmp(self):
        return

    def jmpeq(self):
        return

    def hlt(self):
        return
