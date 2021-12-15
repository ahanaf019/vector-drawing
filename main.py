from VectorDrawing import VectorDrawing
import math
import Vector3D as v3

vd = VectorDrawing()
vd.draw_axis()
vd.make_grid()

points = {(1,1),(2,2),(3,3)}
vd.plot_points(points)
vd.connect_points(points)
vd.plot_polar_point(15, 0)


input()
