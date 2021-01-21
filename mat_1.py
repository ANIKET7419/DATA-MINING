import matplotlib.pyplot as p
p.axis([0,50,0,160])
p.title("Draw a line")
y_points=[3*x for x in range(0,51)]
x_points=range(0,51)
p.xlabel('X-axis')
p.ylabel('Y-axis')
p.plot(x_points,y_points)
p.show()