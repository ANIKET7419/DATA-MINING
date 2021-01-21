import matplotlib.pyplot as p
p.title("Closing stock value of Alphabet Inc ")
p.xlabel('Date')
p.ylabel('Closing Value')
p.yticks([772.5,773.0,773.5,774.0,774.5,775.0,775.5,776.0,776.5,777.0])
p.plot(['2016-10-03','2016-10-04','2016-10-05','2016-10-06','2016-10-07'],[772.5599,776.4299,776.46997,776.859985,775.0800],'ro-')
p.grid(color='b')
p.show()