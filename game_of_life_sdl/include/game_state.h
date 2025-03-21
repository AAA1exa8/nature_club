#ifndef GAME_STATE_H
#define GAME_STATE_H

#include "grid.h"
#include <stdbool.h>

typedef struct {
  Grid *grid;
  bool paused;
  bool mouseDown;
} GameState;

GameState *createGameState();
void destroyGameState(GameState *gameState);

#endif // GAME_STATE_H
