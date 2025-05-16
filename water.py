import math
import sys
from random import randint, random

import pygame
from pygame import Vector2 as Point

# RUNTIME CONFIGURATIONS
FPS = 60
GRAVITY = 500  # pixels per second squared

pygame.init()
screen_width = 1200
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Water')
clock = pygame.time.Clock()

class Rock:
    def __init__(self, x, y):
        self.radius = randint(10, 30)
        self.position = Point(x, y)
        self.velocity = Point(0, 0)
        self.splashed = False

    def update(self, dt):
        # simple gravity
        self.velocity.y += GRAVITY * dt
        self.position += self.velocity * dt

    def draw(self, surf):
        pygame.draw.circle(surf, 'deeppink2', (int(self.position.x), int(self.position.y)), self.radius)

class WaterSpring:
    def __init__(self, x, target_height=None):
        self.target_height = target_height or (screen_height // 2 + 150)
        self.dampening = 0.05
        self.tension = 0.01
        self.height = self.target_height
        self.vel = 0
        self.x = x

    def update(self):
        dh = self.target_height - self.height
        if abs(dh) < 0.01:
            self.height = self.target_height
        self.vel += self.tension * dh - self.vel * self.dampening
        self.height += self.vel

    def draw(self, surf):
        pygame.draw.circle(surf, 'white', (self.x, int(self.height)), 1)

class Wave:
    def __init__(self):
        diff = 20
        self.diff = diff
        self.springs = [WaterSpring(x=i * diff) for i in range(screen_width // diff + 2)]
        self.points = []

    def get_spring_index_for_x_pos(self, x):
        return int(x // self.diff)

    def get_target_height(self):
        return self.springs[0].target_height

    def set_target_height(self, height):
        for spring in self.springs:
            spring.target_height = height

    def add_volume(self, volume):
        delta = volume / screen_width
        self.set_target_height(self.get_target_height() - delta)

    def update(self):
        for spring in self.springs:
            spring.update()
        self.spread_wave()
        self.points = [Point(s.x, s.height) for s in self.springs]
        self.points.append(Point(screen_width, screen_height))
        self.points.append(Point(0, screen_height))

    def draw(self, surf):
        pygame.draw.polygon(surf, (0, 0, 255, 50), [(p.x, p.y) for p in self.points])

    def draw_line(self, surf):
        pygame.draw.lines(surf, 'white', False, [(p.x, p.y) for p in self.points[:-2]], 3)

    def spread_wave(self):
        spread = 0.1
        for i, spring in enumerate(self.springs):
            if i > 0:
                left = self.springs[i - 1]
                left.vel += spread * (spring.height - left.height)
            if i < len(self.springs) - 1:
                right = self.springs[i + 1]
                right.vel += spread * (spring.height - right.height)

    def splash(self, index, vel):
        if 0 <= index < len(self.springs):
            self.springs[index].vel += vel


def handle_rock_collisions(rocks):
    for i in range(len(rocks)):
        for j in range(i + 1, len(rocks)):
            r1 = rocks[i]
            r2 = rocks[j]
            delta = r2.position - r1.position
            dist = delta.length()
            min_dist = r1.radius + r2.radius
            if dist < min_dist and dist > 0:
                # resolve overlap
                overlap = 0.5 * (min_dist - dist)
                norm = delta / dist
                r1.position -= norm * overlap
                r2.position += norm * overlap
                # simple elastic swap of velocities
                v1 = r1.velocity.copy()
                r1.velocity = r2.velocity
                r2.velocity = v1


def main():
    rocks = []
    wave = Wave()
    overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

    while True:
        dt = clock.get_time() / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_r:
                    rocks.append(Rock(screen_width // 2, 0))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = pygame.mouse.get_pos()
                rocks.append(Rock(mx, my))

        # update rocks
        screen.fill('darkslategray1')
        # rock-rock collisions
        handle_rock_collisions(rocks)
        for rock in rocks:
            rock.update(dt)
            # ground collision: stop at bottom
            if rock.position.y + rock.radius > screen_height:
                rock.position.y = screen_height - rock.radius
                rock.velocity.y = 0
            # check for splash onto water
            if not rock.splashed and rock.position.y + rock.radius > wave.get_target_height():
                rock.splashed = True
                idx = wave.get_spring_index_for_x_pos(rock.position.x)
                wave.splash(idx, rock.radius)
                wave.add_volume(math.pi * rock.radius ** 2)
            rock.draw(screen)


        wave.update()

        overlay.fill((0, 0, 0, 0))

        # draw water
        wave.draw(overlay)
        screen.blit(overlay, (0, 0))
        wave.draw_line(screen)


        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    main()

