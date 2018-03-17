import simpy
import world
import display
import threading

env = simpy.rt.RealtimeEnvironment(initial_time=0, factor=1/30, strict=False)


def simulate():
    display.init_screen()
    world.init_people(20)
    threading.Thread(target=env_run).start()
    game_loop()


def env_run():
    env.run()


def game_loop():
    while not world.done:
        display.check_input()
        display.render()


