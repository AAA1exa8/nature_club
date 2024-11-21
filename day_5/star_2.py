from itertools import chain

def main():
    input_file = "./input.txt"
    with open(input_file, 'r') as file:
        input_data = file.read().strip().split("\n\n")

    seeds = list(map(int, input_data[0].split(": ")[1].split(" ")))
    seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

    maps = []
    for section in input_data[1:]:
        map_section = []
        for line in section.split("\n")[1:]:
            parts = list(map(int, line.split(" ")))
            map_section.append((parts[0], parts[1], parts[2]))
        map_section.sort(key=lambda x: x[1])
        maps.append(map_section)

    def transform_low_high(low_high, map_section):
        low, high = low_high
        shranges = []
        result = []
        for dest, source, length in map_section:
            end = source + length - 1
            diff = dest - source
            if not (source > high or end < low):
                shranges.append((max(source, low), min(end, high), diff))
        
        for i, (low, high, diff) in enumerate(shranges):
            result.append((low + diff, high + diff))
            if i < len(shranges) - 1 and shranges[i + 1][0] > high + 1:
                result.append((high + 1, shranges[i + 1][0] - 1))
        
        if not shranges:
            result.append((low, high))
            return result
        
        if shranges[0][0] != low:
            result.append((low, shranges[0][0] - 1))
        
        if shranges[-1][1] != high:
            result.append((shranges[-1][1] + 1, high))
        
        return result

    output = float('inf')
    for low, length in seeds:
        cur = [(low, low + length - 1)]
        new = []
        for map_section in maps:
            for low, high in cur:
                new.extend(transform_low_high((low, high), map_section))
            cur = new
            new = []
        for low, high in cur:
            output = min(output, low)
    
    print(output)

if __name__ == "__main__":
    main()