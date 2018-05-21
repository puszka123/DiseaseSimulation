# człowiek nie wybiera choroby, to choroba wybiera człowieka

import world
from settings import TILESIZE
from utils import distance
from random import *
import time


random10 = Random()


class Infection:
    def __init__(self, env, person, population, infections):
        self.env = env
        self.person = person
        self.population = population
        self.infections = infections
        self.timeWhenInfected = time.time()

        env.process(self.live())

    def live(self):
        while not world.done:
            for person in self.population:
                if time.time() > person.last_made_contact + 3:
                    if person.infection <= 0:
                        if distance(person.pos, self.person.pos) <= TILESIZE:
                            if person.resistance <= random10.randint(1, 100):
                                self.infections.append(Infection(self.env, person, self.population, self.infections))
                            person.last_made_contact = time.time()

            if not self.person.infection >= 255:
                self.person.infection += 10
            if self.person.infection > 255:
                self.person.infection = 255

            if time.time() > self.timeWhenInfected + 30 + random10.randint(0,20):
                self.person.dead = True

            yield self.env.timeout(1)
