from random import randint
import person
import simulation
import infection
from settings import GRIDWIDTH, GRIDHEIGHT, TILESIZE
from os import path
from map import Map


population = []
circle_radius = 16
width, height = 1024, 768
done = False
grass = []
walkpath = []
road =[]
game = None
tilemap = None


def init_population(number_of_people):
    global population, tilemap
    for i in range(number_of_people):
        population += [person.Person(simulation.env, i, population, tilemap.width, tilemap.height)]
    infections = []
    for m in population:
        if randint(0, 100) < 2:
            infections.append(infection.Infection(simulation.env, m, population, infections))


def init_world():
    global grass, walkpath, road, tilemap
    load_data()
    for col, tiles in enumerate(tilemap.data):
        for row, tile in enumerate(tiles):
            if tile == '2':
                grass.append([row, col])
            elif tile == '0':
                walkpath.append([row, col])
            elif tile == '1':
                road.append([row, col])


def load_data():
    global tilemap
    game_folder = path.dirname(__file__)
    tilemap = Map(path.join(game_folder, 'map.txt'))
    tilemap.convert_tilemap('map/map.txt')


def get_population():
    global population
    return population


def get_done():
    global done
    return done
