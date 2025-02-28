import random
import time
import copy

class Game:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.game = [[random.random() > 0.5 for _ in range(width)] for _ in range(height)]

    def __str__(self):
        return '\n'.join([''.join(['#' if cell else '.' for cell in row]) for row in self.game])

    def get_neighbor_count(self, x: int, y: int):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                nx, ny = x + i, y + j
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    count += self.game[ny][nx]
        return count

    def update(self):
        new_game = copy.deepcopy(self.game)  # Create a copy to store new states

        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.get_neighbor_count(x, y)
                if self.game[y][x]:  # Alive cell
                    new_game[y][x] = neighbors in (2, 3)  # Survives if 2 or 3 neighbors
                else:  # Dead cell
                    new_game[y][x] = neighbors == 3  # Becomes alive if exactly 3 neighbors

        self.game = new_game  # Replace the old grid with the updated one

def main():
    game = Game(10, 10)
    print(game)
    print()
    while True:
        time.sleep(1)
        game.update()
        print(game)
        print()

if __name__ == '__main__':
    main()

