from random import randint
import person
import simulation
import infection

population = []
circle_radius = 16
width, height = 1024, 768
done = False


def init_population(number_of_people):
    global population
    for i in range(number_of_people):
        population += [person.Person(simulation.env, [randint(circle_radius, width - circle_radius),
                                                      randint(circle_radius, height - circle_radius)])]
    infections = []
    for m in population:
        if randint(0, 100) < 10:
            infections.append(infection.Infection(simulation.env, m, population, infections))


def get_population():
    global population
    return population


def get_done():
    global done
    return done
