import math


class Vector3D:

    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]
        self.z = point[2]


def add(v1, v2):
    return [v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2]]


def subtract(v1, v2):
    return add(v1, scaler_multiply(v2, -1))


def scaler_multiply(v, m):
    return [v1 * m for v1 in v]


def dot_product(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]


def translate(point, vector):
    return add(point, vector)


def angles_between(v1, v2):
    return math.acos(dot_product(v1,v2) )


def length(v1):
    return math.sqrt(v1[0] ** 2 + v1[1] ** 2 + v1[2] ** 2)
