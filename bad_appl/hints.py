import struct


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


def show(self):
    data = self.memory[0:64]
    frame = '\n'.join(
        ''.join('  ' if (data[i] << 32 | data[i+1]) &
                (1 << j) else '██' for j in range(64))
        for i in range(0, 64, 2)
    )
    print(frame)
