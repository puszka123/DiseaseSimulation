import simpy
import world
import display
import threading
import pygame_template as pt

env = simpy.rt.RealtimeEnvironment(initial_time=0, factor=1/30, strict=False)


def simulate():
    display.init_screen()
    world.init_world()
    world.init_population(10)
    threading.Thread(target=env_run).start()
    #game_loop()
    world.game = pt.Game()
    world.game.start_gameloop()


def env_run():
    env.run()


def game_loop():
    while not world.done:
        display.check_input()
        display.render()


