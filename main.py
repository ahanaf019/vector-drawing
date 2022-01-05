from VectorDrawing import VectorDrawing
import math
from c_maths import *
import Vector3D as v3

vd = VectorDrawing()
vd.set_units(5,5)
vd.draw_axis()
vd.make_grid()

points = [(1,0.9),(2,2.4),(3,3.5),(4,4.8),(5,5.7)]
vd.plot_points(points)
# vd.connect_points(points)
# vd.plot_polar_point(15, 0)

xy = 0;
xs = 0;
ys = 0;
x2s = 0;

for point in points:
    print(point)
    xs = xs + point[0]
    x2s = x2s + point[0]*point[0]
    ys = ys + point[1]
    xy = xy + point[0]*point[1]
    

n = len(points)    
xbar = xs/n
ybar = ys/n

a1 = (n * xy - xs*ys) / (n * x2s - xs*xs)

a0 = ybar - a1 * xbar


X1 = -100;
Y1 = -a0 + X1 * a1
 
X2 = -100;
X2 = -100;
Y2 = -a0 + X1 * a1
    
vd.set_color('blue')
# vd.draw_line((X1, Y1), (X2, Y2))



# vd.draw_circle((2,2), 5)
  
# vd.refresh()

# # vd.refresh()

point = (3,0)

# while True:
#     point = rotate(point, 60)

points = [(0,1),(1,2),(2,0), (1,-1)]
x = 0
y = 0
while True:
    vd.refresh()
    points = translate((x,y), points)
    for i in range(len(points)):
        # print(point)
        
        points[i] = rotate(points[i], 5)
    vd.plot_points(points)
    vd.connect_points(points)
    x+=0.01
    y+=0.01
    # vd.plot_points(points)
    # vd.gfx_update()






input()
