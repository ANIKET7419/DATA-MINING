import matplotlib.pyplot as p
p.axis([1,3,1,4])
p.title("Sample Graph")
y_points=[2*x for x in range(1,3)]
y_points=y_points+[(-3*x)+10 for x in range(3,4)]
x_points=range(1,4)
p.xlabel('X-axis')
p.ylabel('Y-axis')
p.plot(x_points,y_points)
p.show()