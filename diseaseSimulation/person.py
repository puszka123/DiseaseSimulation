import utils
import collider
import world
from random import randint


class Person:
    def __init__(self, env, pos, idnum):
        self.id = idnum
        self.infection = 0
        self.pos = pos
        self.speed = 10
        self.direction = [0, 0]
        self.env = env
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
            if randint(0, 100) > change_dir_prob:
                w = randint(-self.speed, self.speed)
                h = randint(-self.speed, self.speed)
                #print([w, h])
                self.run([w, h])
            else:
                self.run(self.direction)

            yield self.env.timeout(1)
