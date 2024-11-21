def main():
    input_file = "./input.txt"
    try:
        with open(input_file, 'r') as file:
            input_data = file.read()
    except IOError:
        print("Error reading input file")
        return

    cards = []
    for line in input_data.splitlines():
        card_part, nums = line.split(':')
        card = int(card_part.split()[-1])
        win_part, my_part = nums.split('|')
        win = [int(n) for n in win_part.strip().split() if n.strip()]
        my = [int(n) for n in my_part.strip().split() if n.strip()]
        winning = sum(1 for n in win if n in my)
        cards.append((card, winning))

    copies = [1] * len(cards)
    for i, (card, win) in enumerate(cards):
        for j in range(win):
            copies[j + card] += copies[card - 1]

    print(sum(copies))

if __name__ == "__main__":
    main()