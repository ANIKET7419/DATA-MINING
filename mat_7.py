import matplotlib.pyplot as p
men= [22, 30, 35, 35, 26]
women = [25, 32, 30, 35, 29]
y=[i*5 for i in range(0,8)]
p.xticks(y)
x=['G1','G2','G3','G4','G5']
x_1=range(0,5)
x_2=[ i+.4 for i in range(0,5)]
p.bar(x_1,men,color='green',label='Men',width=0.4)
p.bar(x_2,women,color='red',label='Women',width=0.4)
p.xticks([i+0.2 for i in x_1 ],x)
p.legend()
p.title('Scores by person')
p.xlabel('Person')
p.ylabel('Scores')
p.show()