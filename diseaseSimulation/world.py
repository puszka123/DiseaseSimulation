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

#stats
HOUR = 3600
mean_resistance = 0
deathTime_average = 0
age_average = 0
infection_strength = 50
average_death_time = 1*HOUR



def init_population(number_of_people, infected_people):
    global population, tilemap, mean_resistance, deathTime_average, age_average
    for i in range(number_of_people):
        population += [person.Person(simulation.env, i, population, tilemap.width, tilemap.height)]

    #calculate mean_resistance
    mean_resistance /= number_of_people
    deathTime_average /= number_of_people
    age_average /= number_of_people
    print("number of people: " + str(number_of_people))
    print("number of infected people: " + str(infected_people))
    print("resistance average: " + str(mean_resistance))
    print("death time average: " + str(deathTime_average))
    print("age average: " + str(round(age_average)))
    infections = []
    for m in population:
        if infected_people > 0:
            infections.append(infection.Infection(simulation.env, m, population, infections))
            infected_people -= 1


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
