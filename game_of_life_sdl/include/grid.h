#ifndef GRID_H
#define GRID_H

#include <stdbool.h>

#define WIDTH 40
#define HEIGHT 40

typedef struct {
  bool *cells;
  bool *next;
  bool updated;
} Grid;

Grid *createGrid();
void initGridWidthRandomCells(Grid *grid);
void destroyGrid(Grid *grid);
void setCell(Grid *grid, int x, int y, bool value);
void setNextCell(Grid *grid, int x, int y, bool value);
int getNeighborCells(Grid *grid, int x, int y);
void nextGenGrid(Grid *grid);
void updateGrid(Grid *grid);

#endif // GRID_H
