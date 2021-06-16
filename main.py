from VectorDrawing import VectorDrawing
import math
import Vector3D as v3
# pm1 = [-1, 1]


# vertices = [(x,y,z) for x in pm1 for y in pm1 for z in pm1]
# edges = [((-1,y,z), (1,y,z)) for y in pm1 for z in pm1] +\
#          [((x,-1,z), (x,1,z)) for x in pm1 for z in pm1] +\
#          [((x,y,-1), (x,y,1)) for x in pm1 for y in pm1]
# print(edges)
print(v3.scaler_multiply((1,2,-3), 5))
print(v3.add((1,2,3), (2,-1,4)))
# a = (2,1,-3)
# a = a *5
# print(a)

# vs = [(math.sin(math.pi * t / 6), math.cos(math.pi * t / 6), 1.0/3) for t in range(0,24)]
#
# running_sum = (0, 0, 0)
# arrows = []
# for v in vs:
#     next_sum = v3.add(running_sum, v)
#     arrows.append(Arrow3D(next_sum, running_sum))
#     running_sum = next_sum
# print(running_sum)

vd = VectorDrawing()
#
xunit = 10
yunit = 10
vd.set_units(xunit, yunit)
vd.draw_axis()
vd.make_grid()
# points = []
#
# dino_points = [(6, 4), (5, 1), (3, -1), (1, -2), (2, -3), (1, -4), (-1, -4), (0, -3), (-1, 0), (-2, 1), (-4, 0),
#                (-5, 1), (-2, 2), (-5, 2), (-5, 3), (-4, 4), (-3, 4), (-2, 5), (-1, 5), (1, 2), (3, 1)]

# translations = [(12*x, 10*y) for x in range(-5, 5) for y in range(-5, 5)]

# vd.set_color("blue")
# dinos = [vd.polygon(vd.translate(t, dino_points)) for t in translations]

# vd.plot_points(dino_points)
# vd.polygon(dino_points)
# vd.connect_points(dino_points)

# x = -10
# while x < 11:
#     y = x**2
#     points.append((x, y))
#     x = x + 0.1


# for x in range(-10, 11):
#     y = x**2
#     points.append((x, y))


# vd.plot_points(points)
# vd.connect_points(points)
#
# dino_points2 = [vd.add((10, - 12.5), v) for v in dino_points]
#
# vd.polygon(dino_points2)
# vd.plot_points(dino_points2)
# rotated = dino_points2
# while True:
#     rotated = [vd.rotate(v, -3) for v in rotated]
#     vd.set_color("green")
#     # vd.plot_points(rotated)
#     vd.polygon(rotated)
#     vd.refresh()
# point2 = [(0, 0), (0, 3), (4, 0)]
#
# a = vd.perimeter(dino_points)

# vd.draw_line(2, 1)

# for x in range(-5,5):
#     y = 2 * x + 1
#     vd.plot_point(x,y)


# vd.draw_circle((5, 6), 1.5)
# vd.gfx_update()
# a = vd.intersection(2,1,1,0)
# a = vd.cartesian_to_polar((-4.879, 6.962))
# vd.plot_polar_point(8.5, 125)
#
# vd.draw_line(8, 5)
# vd.x_parallel_line(5)
# vd.y_parallel_line(3)
# vd.gfx_update()
# print(a)
# #

# a = [(math.cos(vd.to_degrees(5 * x * math.pi/500.0)), vd.to_degrees(2 * math.pi * x / 1000.0)) for x in range(-1000, 1000)]
# for x in a:
#     vd.plot_polar_point(x[0], x[1])
#
# vd.gfx_update()
# f = vd.cartesian_to_polar((-2,3))
# print(vd.to_radians(f[1]))

input()
