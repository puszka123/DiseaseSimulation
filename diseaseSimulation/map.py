import pygame
from settings import *
import re


class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line)

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth*TILESIZE
        self.height = self.tileheight*TILESIZE

    def convert_tilemap(self, tilemap_path_txt):
        data = []
        with open(tilemap_path_txt, 'rt') as tilemap:
            for line in tilemap:
                row = line.split(',')
                data.append(row)
        self.data = data
        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH/2)
        y = -target.rect.y + int(HEIGHT/2)
        self.camera = pygame.Rect(x, y, self.width, self.height)