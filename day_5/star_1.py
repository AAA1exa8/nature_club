def main():
    input_file = "./input.txt"
    with open(input_file, 'r') as file:
        input_data = file.read().strip().split("\n\n")

    seeds = list(map(int, input_data[0].split(": ")[1].split(" ")))

    maps = []
    for section in input_data[1:]:
        map_section = []
        for line in section.split("\n")[1:]:
            parts = list(map(int, line.split(" ")))
            map_section.append((parts[0], parts[1], parts[2]))
        maps.append(map_section)

    def transform(seed, maps):
        for map_section in maps:
            for dest, source, length in map_section:
                if source <= seed < source + length:
                    seed = seed + (dest - source)
                    break
        return seed

    output = min(transform(seed, maps) for seed in seeds)

    print(output)

if __name__ == "__main__":
    main()