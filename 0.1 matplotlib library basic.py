
'''
import matplotlib.pyplot as plt

x = [12,32,11,45,67,21]
y = [43,21,90,54,32,11]

plt.plot(x,y,color="green",linestyle="dashdot")
plt.title("temperature vs volume")
plt.xlabel("temperature")
plt.ylabel("volume")
plt.grid(True,color='yellow')
plt.show()

'''
'''
import matplotlib.pyplot as plt

x = [12,32,11,45,67,21]
y = [43,21,90,54,32,11]

plt.plot(x,y)
plt.title("temperature vs volume")
plt.xlabel("temperature")
plt.ylabel("volume")
plt.grid(True,color='yellow')
plt.show()

'''

'''
import matplotlib.pyplot as plt

x = [12,32,11,45,67,21]
y = [43,21,90,54,32,11]

plt.plot(x,y,'ro')
plt.title("temperature vs volume")
plt.xlabel("temperature")
plt.ylabel("volume")
plt.show()
'''
'''
import matplotlib.pyplot as plt

x = [12,32,11,45,67,21]
y = [43,21,90,54,32,11]

plt.plot(x,y,'bs')
plt.title("temperature vs volume")
plt.xlabel("temperature")
plt.ylabel("volume")
plt.show()
'''
'''
import matplotlib.pyplot as plt

x = [12,32,11,45,67,21]
y = [43,21,90,54,32,11]

plt.plot(x,y,'gp')
plt.title("temperature vs volume")
plt.xlabel("temperature")
plt.ylabel("volume")
plt.show()
'''
'''
import matplotlib.pyplot as plt

x = [12,32,11,45,67,21]
y = [43,21,90,54,32,11]

plt.plot(x,y,'yd')
plt.title("temperature vs volume")
plt.xlabel("temperature")
plt.ylabel("volume")
plt.show()
'''

'''
import matplotlib.pyplot as plt

x = [12,32,11,45,67,21]
y = [43,21,90,54,32,11]

plt.plot(x,y,'ro')
plt.plot(x,y,color='green')
plt.title("temperature vs volume")
plt.xlabel("temperature")
plt.ylabel("volume")
plt.show()
'''

'''
import matplotlib.pyplot as plt

x = [12,32,11,45,67,21]
y = [43,21,90,54,32,11]

plt.scatter(x,y)
plt.title("temperature vs volume")
plt.xlabel("temperature")
plt.ylabel("volume")
plt.grid(True,color='red')
plt.show()
'''

'''
import matplotlib.pyplot as plt

x = [12,32,11,45,67,21]
y = [43,21,90,54,32,11]
color=['red','green','blue','yellow','cyan','purple']
plt.scatter(x,y,color=color)
plt.title("temperature vs volume")
plt.xlabel("temperature")
plt.ylabel("volume")
plt.show()
'''

'''
import matplotlib.pyplot as plt

x = [12,32,11,45,67,21]
y = [43,21,90,54,32,11]
color=['red','green','blue','yellow','cyan','purple']
size=[120,150,180,220,630,360]
plt.scatter(x,y,color=color,sizes=size)
plt.title("temperature vs volume")
plt.xlabel("temperature")
plt.ylabel("volume")
plt.grid(True,color='green')
plt.show()

'''
'''
import matplotlib.pyplot as plt
x = ["warsaw",'keev','mogadishu','helsinki','dublin','bern','geneva']
y = [12000,80000,45000,55000,85000,165000,600000]
color=['red','green','blue','yellow','cyan','purple','orange']
plt.bar(x,y,color=color)
plt.show()
'''

'''
import matplotlib.pyplot as plt
x = ["warsaw",'keev','mogadishu','helsinki','dublin','bern','geneva']
y = [12000,80000,45000,55000,85000,165000,60000]
color=['red','green','blue','yellow','cyan','purple','orange']
plt.barh(x,y,color=color)
plt.show()
'''

'''
#autorepeat color
import matplotlib.pyplot as plt
x = ["warsaw",'keev','mogadishu','helsinki','dublin','bern','geneva']
y = [12000,80000,45000,55000,85000,165000,60000]
color=['red','green','blue','yellow']
plt.barh(x,y,color=color)
plt.show()
'''

'''
import matplotlib.pyplot as plt
x = ["warsaw",'keev','mogadishu','helsinki','dublin','bern','geneva']
y = [12000,80000,45000,55000,85000,165000,60000]
color=['red','green','blue','yellow']
plt.bar(x,y,color=color)
plt.plot(x,y,color='black')
plt.grid(True,color='red')
plt.show()
'''

'''
#importing required library
import numpy as np
import matplotlib.pyplot as plt

#creating x axis with range and y axis with sine
#function for plotting sine graph

x = np.arange(0,5*np.pi,0.1)
y = np.cos(x)
plt.grid(True,color='red')

#plotting sine graph
plt.plot(x,y,color='green')
plt.show()
'''

'''
import numpy as np
import matplotlib.pyplot as plt

#creating x axis with range and y axis with sine
#function for plotting sine graph

x = np.arange(0,5*np.pi,0.1)
y = np.sin(x)
plt.grid(True,color='red')

#plotting sine graph
plt.plot(x,y,color='green')
plt.show()
'''

'''
import numpy as np
import matplotlib.pyplot as plt

#creating x axis with range and y axis with sine
#function for plotting sine graph

x = np.arange(0,5*np.pi,0.1)
y = np.tan(x)
plt.grid(True,color='red')

#plotting sine graph
plt.plot(x,y,color='green')
plt.show()
'''


'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,200)
y = np.sin(x)

plt.plot(x,y)
plt.plot(x,y,'--y')
plt.xlabel("this is my data for x axis")
plt.ylabel("this is my data for y axis")
plt.title("this is my title")
plt.show()
'''

'''
import matplotlib.pyplot as plt
import numpy as np
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x,y)
color = np.random.rand(50)
size = np.random.rand(50)*1000
plt.scatter(x,y,color=color,sizes=size,alpha=1)
'''




'''
#rotate x axis labels
import matplotlib.pyplot as plt
x = ["warsaw",'keev','mogadishu','helsinki','dublin','bern','geneva']
y = [12000,80000,45000,55000,85000,165000,60000]
color=['red','green','blue','yellow']
plt.bar(x,y,color=color)
plt.plot(x,y,color='black')
plt.grid(True,color='red')
plt.xticks(rotation=45)
plt.show()

#adjust x axis label frequency
import matplotlib.pyplot as plt
x = ["warsaw",'keev','mogadishu','helsinki','dublin','bern','geneva']
y = [12000,80000,45000,55000,85000,165000,60000]
color=['red','green','blue','yellow']
plt.bar(x,y,color=color)
plt.plot(x,y,color='black')
plt.grid(True,color='red')
plt.xticks([1,3,5])
plt.show()


#use a smaller font size
import matplotlib.pyplot as plt
x = ["warsaw",'keev','mogadishu','helsinki','dublin','bern','geneva']
y = [12000,80000,45000,55000,85000,165000,60000]
color=['red','green','blue','yellow']
plt.bar(x,y,color=color)
plt.plot(x,y,color='black')
plt.grid(True,color='red')
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.show()


#rotation 90
import matplotlib.pyplot as plt
x = ["warsaw",'keev','mogadishu','helsinki','dublin','bern','geneva']
y = [12000,80000,45000,55000,85000,165000,60000]
color=['red','green','blue','yellow']
plt.bar(x,y,color=color)
plt.plot(x,y,color='black')
plt.grid(True,color='red')
plt.xticks(rotation=90)
plt.show()


#roation 120
import matplotlib.pyplot as plt
x = ["warsaw",'keev','mogadishu','helsinki','dublin','bern','geneva']
y = [12000,80000,45000,55000,85000,165000,60000]
color=['red','green','blue','yellow']
plt.bar(x,y,color=color)
plt.plot(x,y,color='black')
plt.grid(True,color='red')
plt.xticks(rotation=120)
plt.yticks(rotation=120)
plt.show()

'''

'''
#histogram
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(1000)


plt.hist(data,bins =30, density=True)

plt.title("histogram of random data")
plt.xlabel("values")
plt.ylabels("frequency")

plt.show()
'''

'''
#pair data graph
import matplotlib.pyplot as plt

years = [2018,2019,2020,2021,2022]
male_population = [500,520,550,580,600]
female_population = [300,320,350,380,420]

plt.plot(years, male_population,label='male')
plt.plot(years, female_population, label='female')
plt.xlabel("year")
plt.ylabel("population")
plt.title("population trend")
plt.legend()
plt.show()


import matplotlib.pyplot as plt
import numpy as np

years = [2018,2019,2020,2021,2022]
male_population = [500,520,550,580,600]
female_population = [300,320,350,380,420]

bar_width = 0.4
x = np.arange(len(years))


plt.bar(x-bar_width/2, male_population, bar_width, label='male')
plt.bar(x+bar_width/2, female_population, bar_width, label='female')
plt.xticks(x,years)
plt.xlabel('year')
plt.ylabel('population')
plt.title('population trend')
plt.legend()
plt.show()
'''

