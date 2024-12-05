from cpu import CPU

def main():
    cpu = CPU(False)
    off = cpu.load_data_at('badappl.bin', 0x40)
    cpu.load_data_at('output.bin', off, True)
    while True:
        cpu.cycle()

if __name__ == '__main__':
    main()