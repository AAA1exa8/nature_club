#include "../include/game_state.h"
#include <stdlib.h>

GameState *createGameState() {
  GameState *gameState = malloc(sizeof(GameState));
  if (!gameState)
    return NULL;

  gameState->grid = createGrid();
  if (!gameState->grid) {
    free(gameState);
    return NULL;
  }

  initGridWidthRandomCells(gameState->grid);
  gameState->paused = false;
  gameState->mouseDown = false;

  return gameState;
}

void destroyGameState(GameState *gameState) {
  destroyGrid(gameState->grid);
  free(gameState);
}
