import turtle
import math
import random
import time


class VectorDrawing:
    speed = 0
    xunit = 10
    yunit = 10

    def __init__(self):
        self.speed = 0
        self.xunit = 10
        self.yunit = 10
        self.color = "red"
        turtle.hideturtle()
        turtle.Screen().title("Vector Drawing")
        turtle.tracer(0, 0)
        turtle.penup()

    def draw_axis(self):
        for i in range(-1, 1):
            turtle.speed(0)
            turtle.penup()
            turtle.setpos(-1000, i)
            turtle.pendown()
            turtle.setpos(1000, i)
            turtle.penup()

            turtle.setpos(i, -1000)
            turtle.pendown()
            turtle.setpos(i, 1000)
            turtle.penup()

    def make_grid(self):

        turtle.speed(0)
        turtle.color("green")

        for i in range(-100, 101):

            if i == 0:
                continue

            p = i * self.xunit
            turtle.penup()
            turtle.setpos(p, -1000)
            turtle.pendown()
            turtle.setpos(p, 1000)
            turtle.penup()

            p = i * self.yunit
            turtle.setpos(-1000, p)
            turtle.pendown()
            turtle.setpos(1000, p)
            turtle.penup()

        turtle.update()

    def set_speed(self, s):
        turtle.speed(s)
        self.speed = s

    def plot_point(self, x, y, size=7):
        turtle.penup()
        turtle.setpos(x * self.xunit, y * self.yunit)
        turtle.dot(size, self.color)
        # turtle.update()

    def set_units(self, a, b):
        self.xunit = a
        self.yunit = b

    def connect(self, v1, v2):
        turtle.color(self.color)
        turtle.setpos(v1[0] * self.xunit, v1[1] * self.yunit)
        turtle.pendown()
        turtle.setpos(v2[0] * self.xunit, v2[1] * self.yunit)
        turtle.penup()
        # turtle.update()

    def polygon(self, points):
        prev = 'a'
        for point in points:
            if prev != 'a':
                self.connect(prev, point)

            else:
                first = point
            prev = point

        self.connect(prev, first)
        self.gfx_update()

    def add(self, v1, v2):
        return v1[0] + v2[0], v1[1] + v2[1]

    def plot_points(self, points):
        for point in points:
            self.plot_point(point[0], point[1])
        turtle.update()

    def set_color(self, clr="red"):
        self.color = clr

    def connect_points(self, points):
        prev = 'a'
        for point in points:
            if prev != 'a':
                self.connect(prev, point)
            prev = point
        turtle.update()

    def scaler_multiple(self, v, m):
        return (v[0] * m, v[1] * m)

    def vector_components(self, v):
        return (v[0], 0), (0, v[1])

    def vector_length(self, v1):
        res = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
        return res

    def translate(self, tv, vectors):
        results = []
        for vector in vectors:
            results.append(self.add(tv, vector))

        return results

    def subtract(self, v1, v2):
        return self.add(v1, self.scaler_multiple(v2, -1))

    def distance(self, v1, v2):
        return math.sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2)

    def perimeter(self, vectors):
        sum = 0
        prev = 'a'
        for vector in vectors:
            if prev != 'a':
                sum += self.distance(prev, vector)
            else:
                first = vector
            prev = vector
        sum += self.distance(prev, first)
        return sum

    def draw_line(self, m, c):
        x1 = -2000
        x2 = 2000
        y1 = m * x1 + c;
        y2 = m * x2 + c;

        self.connect((x1, y1), (x2, y2))
        turtle.update()

    def go_to(self, x, y):
        turtle.setpos(x * self.xunit, y * self.yunit)

    def draw_circle(self, center, radius):
        turtle.color(self.color)
        self.plot_point(center[0], center[1])
        self.go_to(center[0], center[1] - radius)
        turtle.pendown()
        turtle.circle(radius * self.xunit)
        turtle.penup()
        turtle.update()

    def intersection(self, m1, c1, m2, c2):
        if m1 - m2 != 0:
            x = -(c1 + c2) / (m1 - m2)
            y = m1 * x + c1
            return (x, y)
        else:
            return None

    def gfx_update(self):
        turtle.update()

    def to_degrees(self, radians):
        return (180 / math.pi) * radians

    def to_radians(self, degrees):
        return (math.pi / 180) * degrees

    def polar_to_cartesian(self, r, angle):
        return (r * math.cos(self.to_radians(angle)), r * math.sin(self.to_radians(angle)))

    def cartesian_to_polar(self, point):
        return self.vector_length(point), self.to_degrees(math.atan2(point[1], point[0]))

    def plot_polar_point(self, r, angle):
        x, y = self.polar_to_cartesian(r, angle)

        self.plot_point(x, y, 2)
        # self.color = "green"
        # self.connect((0,0), (x, y))

    def x_parallel_line(self, a):
        self.connect((a, -2000), (a, 2000))

    def y_parallel_line(self, b):
        self.connect((-2000, b), (2000, b))

    def rotate(self, v, angle):
        r, ang = self.cartesian_to_polar(v)
        print(angle, " ", ang)
        ang += angle
        return self.polar_to_cartesian(r, ang)

    def refresh(self):
        time.sleep(1 / 30)
        turtle.clearscreen()
        turtle.tracer(0, 0)
        turtle.hideturtle()
