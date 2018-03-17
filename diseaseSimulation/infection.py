# człowiek nie wybiera choroby, to choroba wybiera człowieka
import world
from utils import distance


class Infection:
    def __init__(self, env, person, population, infections):
        self.env = env
        self.person = person
        self.population = population
        self.infections = infections

        env.process(self.live())

    def live(self):
        while not world.done:
            for person in self.population:
                if person.infection <= 0:
                    if distance(person.pos, self.person.pos) <= 2 * world.circle_radius:
                        self.infections.append(Infection(self.env, person, self.population, self.infections))
            if not self.person.infection >= 255:
                self.person.infection += 10
            if self.person.infection > 255:
                self.person.infection = 255
            yield self.env.timeout(1)
