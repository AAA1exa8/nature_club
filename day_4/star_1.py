def main():
    input_file = "./input.txt"
    try:
        with open(input_file, 'r') as file:
            input_data = file.read()
    except IOError:
        print("Error reading input file")
        return

    output = sum(
        2 ** (len(set(win) & set(my)) - 1) if len(set(win) & set(my)) > 0 else 0
        for line in input_data.splitlines()
        if (parts := line.split(':')) and len(parts) == 2
        if (nums := parts[1].split('|')) and len(nums) == 2
        if (win := [int(n) for n in nums[0].strip().split() if n.strip()])
        if (my := [int(n) for n in nums[1].strip().split() if n.strip()])
    )

    print(output)

if __name__ == "__main__":
    main()