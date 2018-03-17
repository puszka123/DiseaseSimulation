from random import randint
import display
import man
import simulation
import infection

people = []
circle_radius = 16
width, height = 1024, 768
done = False


def init_people(number_of_people):
    global people
    healthy = []
    for i in range(number_of_people):
        people += [man.Man(simulation.env, [randint(circle_radius, width - circle_radius),
                                            randint(circle_radius, height - circle_radius)])]
    infected = []
    for m in people:
        if randint(0, 100) < 10:
            infected.append(m)
        else:
            healthy.append(m)
    print(infected)
    infect = infection.Infection(simulation.env, infected, healthy)


def get_people():
    global people
    return people

def get_done():
    global done
    return done