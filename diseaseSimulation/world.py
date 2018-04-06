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
walls = []
game = None
tilemap = None


def init_population(number_of_people):
    global population
    for i in range(number_of_people):
        population += [person.Person(simulation.env, [randint(0, GRIDWIDTH*TILESIZE),
                                                      randint(0, GRIDHEIGHT*TILESIZE)], i)]
    infections = []
    for m in population:
        if randint(0, 100) < 10:
            infections.append(infection.Infection(simulation.env, m, population, infections))


def init_world():
    global walls, tilemap
    load_data()
    for row, tiles in enumerate(tilemap.data):
        for col, tile in enumerate(tiles):
            if tile == '1':
                walls.append([row, col])
    print(walls)


def load_data():
    global tilemap
    game_folder = path.dirname(__file__)
    tilemap = Map(path.join(game_folder, 'map.txt'))


def get_population():
    global population
    return population


def get_done():
    global done
    return done
