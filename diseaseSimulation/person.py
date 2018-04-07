import math

import time

import utils
import collider
import world
from random import randint

from settings import *


class Person:
    def __init__(self, env, idnum, population, map_width, map_height):
        self.id = idnum
        self.infection = 0
        self.map_width = map_width
        self.map_height = map_height

        rand_pos = None
        while True:
            rand_pos = [randint(TILESIZE + 1, map_width - TILESIZE * 5 - 1),
                        randint(TILESIZE + 1, map_height - TILESIZE * 5 - 1)]
            if not (collider.collide_with_walls(self.id, rand_pos)):
                break
        self.pos = rand_pos

        self.speed = 10
        self.direction = [0, 0]
        self.env = env
        self.population = population
        env.process(self.live())

        self.timer = time.time()
        self.pos_at_time = self.pos
        self.bored = False

    def run(self, direction):
        newpos = utils.add_vectors(self.pos, direction)
        if not collider.is_out_of_map(newpos):
            if not collider.collide_with_walls(self.id, newpos):
                self.pos = newpos
                self.direction = direction

    def live(self):
        change_dir_prob = 80
        while not world.done:
            if time.time() > self.timer + randint(4, 20):

                if self.bored is True:
                    self.bored = False
                elif self.bored is False:
                    self.bored = True
                self.timer = time.time()
                self.pos_at_time = self.pos

            # run
            if self.infection > 200 and randint(0, 100) < 40 and not self.bored:
                closest_person = None
                closest_dist = float("inf")
                for person in self.population:
                    if person != self and person.infection < 100 and utils.distance(self.pos,
                                                                                    person.pos) < closest_dist:
                        closest_person = person
                        closest_dist = utils.distance(self.pos, person.pos)

                if closest_person is not None:
                    dist_vec = [closest_person.pos[0] - self.pos[0], closest_person.pos[1] - self.pos[1]]
                    norm = math.sqrt(dist_vec[0] ** 2 + dist_vec[1] ** 2)
                    direction = [dist_vec[0] / norm, dist_vec[1] / norm]
                    follow_vec = [direction[0] * self.speed, direction[1] * self.speed]

                    self.run(follow_vec)

            elif randint(0, 100) > change_dir_prob:
                w = randint(-self.speed, self.speed)
                h = randint(-self.speed, self.speed)
                # print([w, h])
                self.run([w, h])
            else:
                self.run(self.direction)

            yield self.env.timeout(1)
