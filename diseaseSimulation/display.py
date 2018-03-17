
import pygame

import world

screen = None


def init_screen():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((world.width, world.height))


def screen_size():
    return pygame.display.get_surface().get_size()


def check_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            world.done = True


def render():
    global screen
    screen.fill((0, 150, 0))
    for person in world.get_population():
        pygame.draw.circle(screen, (person.infection, 0, 255 - person.infection), person.pos, world.circle_radius)
    pygame.display.flip()
