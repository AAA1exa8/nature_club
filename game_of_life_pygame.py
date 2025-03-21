import random
import time
import copy
import pygame

# Define some constants for the display and colors
CELL_SIZE = 20
ALIVE_COLOR = (0, 0, 0)   # Green for alive cells
DEAD_COLOR = (255, 255, 255)      # Black for dead cells
GRID_COLOR = (40, 40, 40)   # Optional grid color

class Game:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.game = [[random.random() > 0.5 for _ in range(width)] for _ in range(height)]

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

def draw_grid(screen, game):
    # Fill the background
    screen.fill(DEAD_COLOR)
    
    for y in range(game.height):
        for x in range(game.width):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if game.game[y][x]:
                pygame.draw.rect(screen, ALIVE_COLOR, rect)

def main():
    # Set grid dimensions
    grid_width, grid_height = 30, 20  # Adjust these values as needed

    # Initialize the game instance
    game_instance = Game(grid_width, grid_height)

    # Initialize PyGame
    pygame.init()
    screen_width = grid_width * CELL_SIZE
    screen_height = grid_height * CELL_SIZE
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Game of Life with PyGame")
    clock = pygame.time.Clock()

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game state
        game_instance.update()

        # Draw the current game state
        draw_grid(screen, game_instance)
        pygame.display.flip()

        # Control the frame rate (e.g., 5 frames per second)
        clock.tick(5)

    pygame.quit()

if __name__ == '__main__':
    main()

