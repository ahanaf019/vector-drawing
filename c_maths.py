
import math

def to_degrees(radians):
    return (180 / math.pi) * radians

def to_radians(degrees):
    return (math.pi / 180) * degrees

def polar_to_cartesian(r, angle):
    return (r * math.cos(to_radians(angle)), r * math.sin(to_radians(angle)))

def cartesian_to_polar(point):
    return vector_length(point), to_degrees(math.atan2(point[1], point[0]))

def scaler_multiple(v, m):
    return (v[0] * m, v[1] * m)

def vector_components(v):
    return (v[0], 0), (0, v[1])

def vector_length(v1):
    res = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
    return res

def translate(tv, vectors):
    results = []
    for vector in vectors:
        results.append(add(tv, vector))

    return results

def subtract(v1, v2):
    return add(v1, scaler_multiple(v2, -1))

def distance(v1, v2):
    return math.sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2)

def perimeter(vectors):
    sum = 0
    prev = 'a'
    for vector in vectors:
        if prev != 'a':
            sum += distance(prev, vector)
        else:
            first = vector
        prev = vector
    sum += distance(prev, first)
    return sum

def add(v1, v2):
    return v1[0] + v2[0], v1[1] + v2[1]

def rotate(v, angle):
    r, ang = cartesian_to_polar(v)
    print(angle, " ", ang)
    ang += angle
    print(polar_to_cartesian(r, ang))
    return polar_to_cartesian(r, ang)