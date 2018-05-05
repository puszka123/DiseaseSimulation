import pygame

pygame.init()
infoObject = pygame.display.Info()
WIDTH = 800
HEIGHT = 600
#FPS = 30
TITLE = 'The simulation of infection'
TILESIZE = 8
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
CAMERA_SPEED = 128
SCALE = 8