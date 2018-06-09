import simpy
import world
import display
import threading
import pygame_template as pt
from monitor import *

env = simpy.rt.RealtimeEnvironment(initial_time=0, factor=1/100, strict=False)

number_of_people = 200
infected_people = 1


def simulate():
    display.init_screen()
    world.init_world()
    world.init_population(number_of_people, infected_people)
    env.process(monitor_simulation())
    threading.Thread(target=env_run).start()
    #game_loop()
    world.game = pt.Game()
    world.game.start_gameloop()


def env_run():
    env.run()


def monitor_simulation():
    # save stats
    interval = 600
    while True:
        inf_count = 0
        healthy_count = 0
        dead_count = 0
        if interval <= 0:
            interval = 600
            for person in world.population:
                if person.dead:
                    dead_count = dead_count + 1
                elif person.infection == 255:
                    inf_count = inf_count + 1
                else:
                    healthy_count = healthy_count + 1
            save_stats(healthy_count, inf_count, dead_count, env.now)
        interval -= 1
        yield env.timeout(1)


def game_loop():
    while not world.done:
        display.check_input()
        display.render()


