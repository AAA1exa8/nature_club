class Game:
    def __init__(self, game_id):
        self.id = game_id
        self.values = []

def parse_input(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read().strip()

    games = []
    for line in input_data.split('\n'):
        id_part, values_part = line.split(': ')
        game_id = int(id_part.split(' ')[1])
        rounds = values_part.split(';')
        
        game = Game(game_id)
        for round in rounds:
            colors = round.split(',')
            r = {'red': 0, 'blue': 0, 'green': 0}
            for color in colors:
                number, color_name = color.strip().split(" ")
                number = int(number)
                if color_name == "red":
                    r['red'] = number
                elif color_name == "blue":
                    r['blue'] = number
                elif color_name == "green":
                    r['green'] = number
                else:
                    raise ValueError(f"Invalid color: {color_name}")
            game.values.append(r)
        games.append(game)
    
    return games

def calculate_output(games):
    output = 0
    for game in games:
        max_red = max((r['red'] for r in game.values), default=0)
        max_blue = max((r['blue'] for r in game.values), default=0)
        max_green = max((r['green'] for r in game.values), default=0)
        output += max_red * max_blue * max_green
    return output

def main():
    games = parse_input('./input.txt')
    output = calculate_output(games)
    print(output)

main()
