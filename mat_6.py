import matplotlib.pyplot as p
x_=[22.2, 17.6, 8.8, 8, 7.7, 6.7]
y_=['Java','Python','PHP','JavaScript','C#','C++']
p.xticks(x_)
l=p.barh(y_,x_,0.5,color=['red','green','yellow','pink','black','grey'],edgecolor='blue')
p.margins(y=0.3)
x=[i.get_width() for i in l]
for y in range(0,6):
    p.text(x[y]+.278,y,s=str(x_[y]),va='center')
p.show()