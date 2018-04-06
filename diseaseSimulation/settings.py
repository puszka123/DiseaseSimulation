import pygame

pygame.init()
infoObject = pygame.display.Info()
WIDTH = infoObject.current_w
HEIGHT = infoObject.current_h
#FPS = 30
TITLE = 'The simulation of infection'
TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
CAMERA_SPEED = 64
SCALE = 8