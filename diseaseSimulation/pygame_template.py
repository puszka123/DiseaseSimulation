import pygame
import world
from settings import *
import settings
import map
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)

class Cameraman(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.rect = pygame.Rect(0,0,TILESIZE,TILESIZE)
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.x = 0
        self.y = 0

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y


class Player(pygame.sprite.Sprite):
    def __init__(self, idnum, person):
        self.person = person
        self.id = idnum
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)

    def update(self):
        self.rect.x = world.get_population()[self.id].pos[0]
        self.rect.y = world.get_population()[self.id].pos[1]
        self.image.fill((self.person.infection, 0, 255 - self.person.infection))
        #print(world.get_population()[0].pos)


class TerrainElement(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((TILESIZE, TILESIZE))
        #self.image.fill((100, 100, 100))
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x*TILESIZE
        self.rect.y = y * TILESIZE


class Game:
    def __init__(self):
        pygame.init()
        #sound
        #pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        #FPS controller
        #clock = pygame.time.Clock()
        pygame.key.set_repeat(200, 100)

        self.all_sprites = pygame.sprite.Group()
        self.players = []
        self.grass = []
        self.walkpath = []
        self.road = []
        #player = Player(world.get_population()[0].id)
        #self.load_data()
        self.init_map()
        #self.all_sprites.add(player)
        #self.players.append(player)
        self.cameraman = Cameraman()
        #self.all_sprites.add(self.cameraman)
        self.camera = map.Camera(world.tilemap.width, world.tilemap.height)

    def init_map(self):
        for grass in world.grass:
            self.grass.append(TerrainElement(grass[0], grass[1], "images/grass.png"))
        self.all_sprites.add(self.grass)
        for walkpath in world.walkpath:
            self.walkpath.append(TerrainElement(walkpath[0], walkpath[1], "images/walkpath.png"))
        self.all_sprites.add(self.walkpath)
        for road in world.road:
            self.road.append(TerrainElement(road[0], road[1], "images/road.png"))
        self.all_sprites.add(self.road)
        for person in world.get_population():
            self.players.append(Player(person.id, person))
        self.all_sprites.add(self.players)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, (0, 100, 0), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, (0, 100, 0), (0, y), (WIDTH, y))

    def start_gameloop(self):
        #Game loop
        while not world.done:
            #Process input
            self.check_input()
            #Update
            self.all_sprites.update()
            self.cameraman.update()
            self.camera.update(self.cameraman)
            #Render
            self.screen.fill((0, 150, 0))
            #self.draw_grid()
            #self.all_sprites.draw(self.screen)
            for sprite in self.all_sprites:
                self.screen.blit(pygame.transform.scale(sprite.image, (TILESIZE, TILESIZE)), self.camera.apply(sprite))
            #always last command(double buffering)
            pygame.display.flip()
        pygame.quit()

    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                world.done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    world.done = True
                if event.key == pygame.K_LEFT:
                    self.cameraman.x -= CAMERA_SPEED
                if event.key == pygame.K_RIGHT:
                    self.cameraman.x += CAMERA_SPEED
                if event.key == pygame.K_UP:
                    self.cameraman.y -= CAMERA_SPEED
                if event.key == pygame.K_DOWN:
                    self.cameraman.y += CAMERA_SPEED
                if event.key == pygame.K_KP_PLUS:
                    pass
                    #settings.TILESIZE += SCALE
                if event.key == pygame.K_KP_MINUS:
                    pass
                    #settings.TILESIZE -= SCALE



    #def collision_with_walls(self, person_id, newpos):
     #   self.players[person_id].rect.topleft = newpos
     #   return pygame.sprite.spritecollideany(self.players[person_id], self.walls)