import matplotlib.pyplot as p
y_=[22.2, 17.6, 8.8, 8, 7.7, 6.7]
p.yticks(y_)
l=p.bar(['Java','Python','PHP','JavaScript','C#','C++'],y_,color=['red','green','yellow','pink','black','grey'],edgecolor='blue',width=0.5)
y=[i.get_height() for i in l]
for x in range(0,6):
    p.text(x,y[x]+.278,s=str(y_[x]),ha='center')
p.show()