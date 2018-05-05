import math

import time

import utils
import collider
import world
from random import *

from settings import *

class Position:
    def __init__(self, x, y):
        self.x = 0
        self.y = 0

class Person:
    def __init__(self, env, idnum, population, map_width, map_height):
        self.id = idnum
        self.infection = 0
        self.map_width = map_width
        self.map_height = map_height
        self.path = list()
        self.on_path = False
        self.path_count = 0
        self.follow_road = True
        self.prev_pos = (-1,-1)

        rand_pos = None
        while True:
            x = randint(TILESIZE + 1, map_width - TILESIZE * 5 - 1)
            y = randint(TILESIZE + 1, map_height - TILESIZE * 5 - 1)

            x = x - x%TILESIZE
            y = y - y%TILESIZE
            rand_pos = [x,y]

            #if not (collider.collide_with_walls(self.id, rand_pos)):
            #    break
            if world.tilemap.data[int(y/TILESIZE)][int(x/TILESIZE)] == '0':
                break
        self.pos = rand_pos

        self.speed = TILESIZE
        self.direction = [0, 0]
        self.env = env
        self.population = population
        env.process(self.live())

        self.timer = time.time()

        self.tick_timer = time.time()
        self.pos_at_time = self.pos
        self.bored = False

        #self.path = self.bfs(int(self.pos[0]/TILESIZE),int(self.pos[1]/TILESIZE),8,8)

        #print(self.path)
        self.on_path = False

    def myround(self, x, base=5):
        return int(base * round(float(x) / base))

    def run(self, direction):
        direction = [self.myround(direction[0], TILESIZE),self.myround(direction[1], TILESIZE)]

        newpos = utils.add_vectors(self.pos, direction)
        if not collider.is_out_of_map(newpos):
            if not collider.collide_with_walls(self.id, newpos):
                self.pos = newpos
                self.direction = direction

    def live(self):
        change_dir_prob = 80
        while not world.done:
            # if time.time() > self.timer + randint(4, 8):
            #
            #     if self.bored is True:
            #         self.bored = False
            #     else:
            #         self.bored = True
            #
            #     self.pos_at_time = self.pos
            #     self.timer = time.time()

            # run
            # self.bored = False

            # if self.infection >= 0 and not self.bored:
            #     closest_person = None
            #     closest_dist = float("inf")
            #     for person in self.population:
            #         if person != self and person.infection < 100 and utils.distance(self.pos,
            #                                                                         person.pos) < closest_dist:
            #             closest_person = person
            #             closest_dist = utils.distance(self.pos, person.pos)
            #
            #     #if closest_person is not None:
            #     dist_vec = [500 - self.pos[0], 500 - self.pos[1]]
            #     norm = math.sqrt(dist_vec[0] ** 2 + dist_vec[1] ** 2)
            #     direction = [dist_vec[0] / norm, dist_vec[1] / norm]
            #     follow_vec = [direction[0] * self.speed, direction[1] * self.speed]
            #
            #     self.run(follow_vec)
            if time.time() > self.tick_timer + 0.1:
                if self.follow_road:
                    map = world.tilemap.data


                    current_pos = (int(self.pos[0]/TILESIZE),int(self.pos[1]/TILESIZE))

                    possible_moves = []

                    if map[current_pos[1]+1][current_pos[0]] == '0' and not (self.prev_pos[0] == current_pos[0] and self.prev_pos[1] == current_pos[1]+1):
                        possible_moves.append((0,TILESIZE))
                    if map[current_pos[1]-1][current_pos[0]] == '0' and not (self.prev_pos[0] == current_pos[0] and self.prev_pos[1] == current_pos[1]-1):
                        possible_moves.append((0, -TILESIZE))
                    if map[current_pos[1]][current_pos[0]+1] == '0' and not (self.prev_pos[0] == current_pos[0]+1 and self.prev_pos[1] == current_pos[1]):
                        possible_moves.append((TILESIZE,0))
                    if map[current_pos[1]][current_pos[0]-1] == '0' and not (self.prev_pos[0] == current_pos[0]-1 and self.prev_pos[1] == current_pos[1]):
                        possible_moves.append((-TILESIZE,0))

                    self.prev_pos = current_pos

                    move = (0,0)
                    if possible_moves:
                        move = choice(possible_moves)

                    self.run(move)
                    #self.run((0,TILESIZE))

                    self.tick_timer = time.time()
                elif not self.on_path:
                    if randint(0, 100) > change_dir_prob:
                        w = randint(-self.speed, self.speed)
                        h = randint(-self.speed, self.speed)
                        # print([w, h])
                        self.run([w, h])
                        self.tick_timer = time.time()
                    #else:
                        #self.run(self.direction)
                else:
                    #print("on path")
                    #print("path len", len(self.path))
                    if self.path_count < len(self.path):
                        #print("path count ", self.path_count)
                        #print("x ", self.path[self.path_count][0], " y ", self.path[self.path_count][1])
                    #     w = self.pos[0] - self.path[self.path_count][0]*TILESIZE
                    #     h = self.pos[1] - self.path[self.path_count][1]*TILESIZE
                    #
                    #     if w > TILESIZE:
                    #         w = TILESIZE
                    #     if w < -TILESIZE:
                    #         w = -TILESIZE
                    #     if h > TILESIZE:
                    #         h = TILESIZE
                    #     if h < -TILESIZE:
                    #         h = -TILESIZE
                    #     print(w)
                    #     print(h)
                        self.path_count = self.path_count + 1
                        if self.pos[0] < 8 * TILESIZE:
                            w = TILESIZE
                        elif self.pos[0] > 8 * TILESIZE:
                            w = -TILESIZE
                        else:
                            w = 0

                        if self.pos[1] < 8 * TILESIZE:
                            h = TILESIZE
                        elif self.pos[1] > 8 * TILESIZE:
                            h = -TILESIZE
                        else:
                            h = 0


                        self.run([w, h])
                        self.tick_timer = time.time()


            yield self.env.timeout(1)

    def bfs(self, x, y, end_x, end_y):
        map = world.tilemap.data

        #for i in range(64-1):
            #print("row ",i)
            #for j in range(64-1):
                #print(map[i][j])

        start = (x,y)

        print("start is ", start)

        # for col, tiles in enumerate(map):
        #     for row, tile in enumerate(tiles):
        #         if tile == '1':
        #             #walls.append([row, col])

        queue = list()
        queue.append([start])

        while queue:
            path = queue.pop(0)

            node = path[-1]

            if node == (end_x,end_y):
                return path

            for adjacent in self.neighbors(map, node):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

    def neighbors(self, map, node):
        nbors = []
        for i in range(-1,2):
            for j in range (-1, 2):
                if map[node[0]+i][node[1]+j] != '1' and not (i == 0 and j == 0):
                    nbors.append((node[0]+i,node[1]+j))
       #print("neighbors of ", node[0], ", ", node[1], " are ", nbors)
        return nbors
