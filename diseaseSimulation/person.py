import utils
import collider
import world
from random import randint


class Person:
    def __init__(self, env, pos):
        self.infection = 0
        self.pos = pos
        self.speed = 3
        self.direction = [0, 0]
        self.env = env
        env.process(self.live())

    def run(self, direction):
        newpos = utils.add_vectors(self.pos, direction)
        if not collider.is_out_of_map(newpos):
            self.direction = direction
            self.pos = newpos

    def live(self):
        change_dir_prob = 80
        while not world.done:
            # run
            if randint(0, 100) > change_dir_prob:
                w = randint(-self.speed, self.speed)
                h = randint(-self.speed, self.speed)
                self.run([w, h])
            else:
                self.run(self.direction)

            yield self.env.timeout(1)
