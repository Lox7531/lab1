"""
X 0.1 0.4 1.0 2.0 6.0 10.0 20.0 40.0 60.0 80.0 100.0
Y 10.9 11.8 12.8 13.4 14.6 15.3 16.4 17.7 18.5 19.2 19.9
"""
'''
import random
random.seed(4)
task1=random.randint(1,24)
print(task1)
'''
import matplotlib.pyplot as plt
import numpy as np
f=open("task_graph.txt","r")
lstX=f.readline()
lstY=f.readline()
f.close()
wordsX=lstX.split()
wordsY=lstY.split()
revX = [float(i) for i in wordsX]
revY = [float(i) for i in wordsY]
print(revX)
print(revY)

plt.style.use('_mpl-gallery')
# size and color:
sizes = np.random.uniform(15, 80, len(revX))
colors = np.random.uniform(15, 80, len(revX))

# plot
fig, ax = plt.subplots()

ax.scatter(revX, revY, s=sizes, c=colors, vmin=0, vmax=100)

ax.set(xlim=(-5, 110), xticks=np.arange(-4, 110),
       ylim=(10, 30), yticks=np.arange(11, 30))

plt.show()
