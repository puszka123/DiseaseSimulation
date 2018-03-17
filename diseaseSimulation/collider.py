import world


def is_out_of_map(pos):
    return pos[0] < world.circle_radius or pos[0] > world.width - world.circle_radius \
           or pos[1] < world.circle_radius or pos[1] > world.height - world.circle_radius
