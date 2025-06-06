#include <SDL3/SDL.h>
#include <SDL3/SDL_events.h>
#include <SDL3/SDL_init.h>
#include <SDL3/SDL_mouse.h>
#include <SDL3/SDL_oldnames.h>
#include <SDL3/SDL_pixels.h>
#include <SDL3/SDL_render.h>
#include <SDL3/SDL_surface.h>
#include <SDL3/SDL_timer.h>
#include <SDL3/SDL_video.h>
#include <stdlib.h>
#include <time.h>

#define SCREEN_WIDTH 800
#define SCREEN_HEIGHT 600
#define MAX_PARTICLES 1000
#define STEP_MILIS 16

typedef struct {
  float x, y;
  float vx, vy;
  float life;
  float r, g, b, a;
} Particle;

Particle particles[MAX_PARTICLES];
SDL_Texture *particle_texture = NULL;

void spawn_particle(int x, int y) {
  for (int i = 0; i < MAX_PARTICLES; ++i) {
    if (particles[i].life <= 0.0f) {
      particles[i].x = x;
      particles[i].y = y;
      particles[i].vx = ((float)(rand() % 200) - 100) / 100.0f;
      particles[i].vy = ((float)(rand() % 200) - 100) / 100.0f - 2.0f;
      particles[i].life = 1.0f;
      particles[i].r = 1.0f;
      particles[i].g = (float)(rand() % 100) / 100.0f;
      particles[i].b = 0.0f;
      particles[i].a = 1.0f;
      break;
    }
  }
}

void update_particles(float dt) {
  for (int i = 0; i < MAX_PARTICLES; ++i) {
    if (particles[i].life > 0.0f) {
      particles[i].vy += 3.0f * dt; // gravity
      particles[i].x += particles[i].vx * 60 * dt;
      particles[i].y += particles[i].vy * 60 * dt;
      particles[i].life -= dt;
      particles[i].a = particles[i].life; // fade out
    }
  }
}

void render_particles(SDL_Renderer *renderer) {
  SDL_SetTextureBlendMode(particle_texture, SDL_BLENDMODE_ADD);
  for (int i = 0; i < MAX_PARTICLES; ++i) {
    if (particles[i].life > 0.0f) {
      SDL_SetTextureColorMod(particle_texture, (Uint8)(particles[i].r * 255),
                             (Uint8)(particles[i].g * 255),
                             (Uint8)(particles[i].b * 255));
      SDL_SetTextureAlphaMod(particle_texture, (Uint8)(particles[i].a * 255));
      SDL_FRect dst = {(int)particles[i].x, (int)particles[i].y, 8, 8};
      SDL_RenderTexture(renderer, particle_texture, NULL, &dst);
    }
  }
}

SDL_Texture *create_particle_texture(SDL_Renderer *renderer) {
  SDL_Surface *surf = SDL_CreateSurface(8, 8, SDL_PIXELFORMAT_RGBA32);
  const SDL_PixelFormatDetails *formatdetail =
      SDL_GetPixelFormatDetails(surf->format);
  SDL_FillSurfaceRect(surf, NULL,
                      SDL_MapRGBA(formatdetail, NULL, 255, 255, 255, 255));
  SDL_Texture *tex = SDL_CreateTextureFromSurface(renderer, surf);
  SDL_DestroySurface(surf);
  return tex;
}

int main(int argc, char *argv[]) {
  if (SDL_SetAppMetadata("2D Particle Sandbox", "0.0.1",
                         "com.example.particles") != true) {
    SDL_Log("Unable to set app metadata: %s", SDL_GetError());
    return 1;
  }

  if (SDL_Init(SDL_INIT_VIDEO | SDL_INIT_EVENTS) != true) {
    SDL_Log("Unable to initialize SDL: %s", SDL_GetError());
    return 1;
  }
  srand((unsigned int)time(NULL));

  SDL_Window *window = SDL_CreateWindow("2D Particle Sandbox", SCREEN_WIDTH,
                                        SCREEN_HEIGHT, SDL_WINDOW_OPENGL);

  if (window == NULL) {
    SDL_Log("Unable to create window: %s", SDL_GetError());
    return 1;
  }

  SDL_Renderer *renderer = SDL_CreateRenderer(window, NULL);
  if (renderer == NULL) {
    SDL_Log("Unable to create renderer: %s", SDL_GetError());
    return 1;
  }

  SDL_SetRenderDrawBlendMode(renderer, SDL_BLENDMODE_BLEND);

  particle_texture = create_particle_texture(renderer);

  int running = 1;
  Uint32 last_time = SDL_GetTicks();

  while (running) {
    SDL_Event event;
    while (SDL_PollEvent(&event)) {
      if (event.type == SDL_EVENT_QUIT)
        running = 0;
    }

    float mouse_x, mouse_y;
    Uint32 mouse_buttons = SDL_GetMouseState(&mouse_x, &mouse_y);
    if (mouse_buttons & SDL_BUTTON_MASK(SDL_BUTTON_LEFT)) {
      for (int i = 0; i < 10; ++i) {
        spawn_particle(mouse_x, mouse_y);
      }
    }

    Uint32 current_time = SDL_GetTicks();
    float dt = (current_time - last_time) / 1000.0f;
    last_time = current_time;

    update_particles(dt);

    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
    SDL_RenderClear(renderer);

    render_particles(renderer);

    SDL_RenderPresent(renderer);
    SDL_Delay(STEP_MILIS);
  }

  SDL_DestroyTexture(particle_texture);
  SDL_DestroyRenderer(renderer);
  SDL_DestroyWindow(window);
  SDL_Quit();

  return 0;
}
