#include "../include/game_state.h"
#include <SDL3/SDL.h>
#include <SDL3/SDL_events.h>
#include <SDL3/SDL_init.h>
#include <SDL3/SDL_keycode.h>
#include <SDL3/SDL_log.h>
#include <SDL3/SDL_mouse.h>
#include <SDL3/SDL_rect.h>
#include <SDL3/SDL_render.h>
#include <SDL3/SDL_video.h>
#include <stdbool.h>
#include <stdio.h>

#define SCALE 10
#define STEP_MILIS 100

int main() {
  if (SDL_SetAppMetadata("Game of Life", "0.0.1", "com.example.gameoflife") !=
      true) {
    SDL_Log("Unable to set app metadata: %s", SDL_GetError());
    return 1;
  }

  if (SDL_Init(SDL_INIT_VIDEO | SDL_INIT_EVENTS) != true) {
    SDL_Log("Unable to initialize SDL: %s", SDL_GetError());
    return 1;
  }

  SDL_Window *window = SDL_CreateWindow("Game of Life", WIDTH * SCALE,
                                        HEIGHT * SCALE, SDL_WINDOW_OPENGL);
  if (window == NULL) {
    SDL_Log("Unable to create window: %s", SDL_GetError());
    return 1;
  }

  SDL_Renderer *renderer = SDL_CreateRenderer(window, NULL);
  if (renderer == NULL) {
    SDL_Log("Unable to create renderer: %s", SDL_GetError());
    return 1;
  }

  GameState *gameState = createGameState();
  if (gameState == NULL) {
    SDL_Log("Unable to create game state");
    return 1;
  }

  bool running = true;
  bool paused = false;
  SDL_Event event;
  while (running) {
    while (SDL_PollEvent(&event)) {
      switch (event.type) {
      case SDL_EVENT_QUIT:
        running = false;
        break;
      case SDL_EVENT_KEY_DOWN:
        switch (event.key.key) {
        case SDLK_SPACE:
          paused = !paused;
          break;
        case SDLK_ESCAPE:
          running = false;
          break;
        }
        break;
      case SDL_EVENT_MOUSE_BUTTON_DOWN:
        if (event.button.button == SDL_BUTTON_LEFT) {
          int x = event.button.x / SCALE;
          int y = event.button.y / SCALE;
          setCell(gameState->grid, x, y, true);
          gameState->mouseDown = true;
        }
        break;
      case SDL_EVENT_MOUSE_BUTTON_UP:
        if (event.button.button == SDL_BUTTON_LEFT) {
          gameState->mouseDown = false;
        }
        break;
      case SDL_EVENT_MOUSE_MOTION:
        if (gameState->mouseDown) {
          int x = event.motion.x / SCALE;
          int y = event.motion.y / SCALE;
          setCell(gameState->grid, x, y, true);
        }
        break;
      }
    }

    if (!paused) {
      nextGenGrid(gameState->grid);
    }
    updateGrid(gameState->grid);

    SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
    SDL_RenderClear(renderer);

    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
    for (int y = 0; y < HEIGHT; y++) {
      for (int x = 0; x < WIDTH; x++) {
        if (gameState->grid->cells[y * WIDTH + x]) {
          SDL_FRect rect = {x * SCALE, y * SCALE, SCALE, SCALE};
          SDL_RenderFillRect(renderer, &rect);
        }
      }
    }

    SDL_RenderPresent(renderer);
    SDL_Delay(STEP_MILIS);
  }

  SDL_DestroyRenderer(renderer);
  SDL_DestroyWindow(window);
  SDL_Quit();
  return 0;
}
