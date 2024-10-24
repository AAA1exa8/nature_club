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

def filter_games(games):
    valid_games = []
    for game in games:
        valid = True
        for value in game.values:
            if (value['red'] or 0) > 12 or (value['blue'] or 0) > 14 or (value['green'] or 0) > 13:
                valid = False
                break
        if valid:
            valid_games.append(game)
    return valid_games

def main():
    games = parse_input('./input.txt')
    valid_games = filter_games(games)
    output = sum(game.id for game in valid_games)
    print(output)

main()
