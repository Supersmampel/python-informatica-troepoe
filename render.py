import cmath
import sys

import numpy as np
import pygame
import time

class Rendering:
    def __init__(self, width, height):
        self.image_width = width
        self.image_height = height
    
    def render(self, print_time=False):
        start_time = time.time()

        # cordinatengrid voor output
        x = np.linspace(0, 1, self.image_width)
        y = np.linspace(0, 1, self.image_height)

        xv, yv = np.meshgrid(x, y)

        # rgb berekenen in np.uint8 0 - 255 gewoon 8bit positieve integer
        r = (255.999 * xv).astype(np.uint8)
        g = (255.999 * yv).astype(np.uint8)
        b = np.zeros_like(r, dtype=np.uint8)

        # plaatje maken met pixels
        image = np.stack((r, g, b), axis=-1)

        # pygame surface maken
        surface = pygame.surfarray.make_surface(image.swapaxes(0, 1))

        if print_time:
            print(f"Done in {time.time() - start_time} seconds.")
        return surface

pygame.init()

renderer = Rendering(255, 255)

image = renderer.render()
screen = pygame.display.set_mode((renderer.image_width, renderer.image_height))

clock = pygame.time.Clock()
tick = 0

running = True
fps_timer = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    screen.blit(renderer.render(), (0, 0))
    pygame.display.flip()
    
    tick = (tick + 1) % 100
    if not tick:
        print(clock.get_fps())
    clock.tick()