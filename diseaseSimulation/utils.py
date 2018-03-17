import math


def add_vectors(a, b):
    if not len(a) == len(b):
        return None
    return [a[0] + b[0], a[1] + b[1]]


def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
