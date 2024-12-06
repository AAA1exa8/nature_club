from cpu import CPU

def main():
    cpu = CPU(False)
    cpu.load_data_at('complete.bin', 0x40)
    while True:
        cpu.cycle()

if __name__ == '__main__':
    main()
