#człowiek nie wybiera choroby, to choroba wybiera człowieka
import world
from utils import distance


class Infection:
    def __init__(self, env, infected, healthy):
        self.env = env
        self.infected = infected
        self.healthy = healthy
        env.process(self.live())

    def live(self):
        while not world.done:
            healthy = []
            infected = []
            for man in self.healthy:
                infect = False
                for inf in self.infected:
                    if distance(man.pos, inf.pos) <= 2*world.circle_radius:
                        man.get_infected()
                        infect = True
                        break
                if infect:
                    infected.append(man)
                else:
                    healthy.append(man)
            self.infected += infected
            self.healthy = healthy
            self.getting_infected()
            yield self.env.timeout(1)

    def getting_infected(self):
        for man in self.infected:
            if not man.infected >= 255:
                man.infected += 10
            if man.infected > 255:
                man.infected = 255
