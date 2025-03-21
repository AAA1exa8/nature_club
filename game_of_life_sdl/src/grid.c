#include "../include/grid.h"
#include <stdlib.h>
#include <string.h>

Grid *createGrid() {
  Grid *grid = malloc(sizeof(Grid));
  if (!grid)
    return NULL;

  grid->cells = calloc(WIDTH * HEIGHT, sizeof(bool));
  grid->next = calloc(WIDTH * HEIGHT, sizeof(bool));
  if (!grid->cells || !grid->next) {
    free(grid->cells);
    free(grid->next);
    free(grid);
    return NULL;
  }

  grid->updated = false;
  return grid;
}

void initGridWidthRandomCells(Grid *grid) {
  for (int y = 0; y < HEIGHT; y++) {
    for (int x = 0; x < WIDTH; x++) {
      grid->cells[y * WIDTH + x] = rand() % 5 == 0;
    }
  }
}

void destroyGrid(Grid *grid) {
  free(grid->cells);
  free(grid->next);
  free(grid);
}

void setCell(Grid *grid, int x, int y, bool value) {
  grid->cells[y * WIDTH + x] = value;
}

void setNextCell(Grid *grid, int x, int y, bool value) {
  grid->next[y * WIDTH + x] = value;
  grid->updated = true;
}

int getNeighborCells(Grid *grid, int x, int y) {
  int count = 0;
  for (int i = -1; i <= 1; i++) {
    for (int j = -1; j <= 1; j++) {
      if (i == 0 && j == 0)
        continue;
      int nx = x + i, ny = y + j;
      if (nx >= 0 && nx < WIDTH && ny >= 0 && ny < HEIGHT) {
        count += grid->cells[ny * WIDTH + nx];
      }
    }
  }
  return count;
}

void nextGenGrid(Grid *grid) {
  for (int y = 0; y < HEIGHT; y++) {
    for (int x = 0; x < WIDTH; x++) {
      int neighbors = getNeighborCells(grid, x, y);
      bool alive = grid->cells[y * WIDTH + x];
      setNextCell(grid, x, y,
                  (alive && (neighbors == 2 || neighbors == 3)) ||
                      (!alive && neighbors == 3));
    }
  }
  grid->updated = true;
}

void updateGrid(Grid *grid) {
  if (grid->updated) {
    memcpy(grid->cells, grid->next, WIDTH * HEIGHT * sizeof(bool));
    grid->updated = false;
  }
}
