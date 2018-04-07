import math

import utils
import collider
import world
from random import randint


class Person:
    def __init__(self, env, pos, idnum, population):
        self.id = idnum
        self.infection = 0
        self.pos = pos
        self.speed = 10
        self.direction = [0, 0]
        self.env = env
        self.population = population
        env.process(self.live())

    def run(self, direction):
        newpos = utils.add_vectors(self.pos, direction)
        if not collider.is_out_of_map(newpos):
            if not collider.collide_with_walls(self.id, newpos):
                self.pos = newpos
                self.direction = direction

    def live(self):
        change_dir_prob = 80
        while not world.done:
            # run
            if self.infection > 200:
                closest_person = None
                closest_dist = float("inf")
                for person in self.population:
                    if person != self and person.infection < 100 and utils.distance(self.pos, person.pos) < closest_dist:
                        closest_person = person
                        closest_dist = utils.distance(self.pos, person.pos)

                if(closest_person != None):
                    dist_vec = [closest_person.pos[0] - self.pos[0], closest_person.pos[1] - self.pos[1]]
                    norm = math.sqrt(dist_vec[0] ** 2 + dist_vec[1] ** 2)
                    direction = [dist_vec[0] / norm, dist_vec[1] / norm]
                    follow_vec = [direction[0] * self.speed, direction[1] * self.speed]

                    self.run(follow_vec)


            elif randint(0, 100) > change_dir_prob:
                w = randint(-self.speed, self.speed)
                h = randint(-self.speed, self.speed)
                #print([w, h])
                self.run([w, h])
            else:
                self.run(self.direction)

            yield self.env.timeout(1)
