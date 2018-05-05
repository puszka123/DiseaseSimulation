import world
from settings import GRIDWIDTH, GRIDHEIGHT, WIDTH, HEIGHT



def is_out_of_map(pos):
    return pos[0] < 0 or pos[0] >= WIDTH or pos[1] < 0 or pos[1] >= HEIGHT


#def collide_with_walls(person_id, newpos):
#    if world.game is not None:
#        return world.game.collision_with_walls(person_id, newpos)
#    else:
#        return False
