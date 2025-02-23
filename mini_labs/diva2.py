'''
import random
random.seed(4)
task1=random.randint(1,24)
print(task1)
'''
import matplotlib.pyplot as plt
import numpy as np
f=open("task.txt","r")
lstX=f.readline()
lstY=f.readline()
f.close()
print(lstX)
words=lstX.split()
rev = [float(i) for i in words]
print(rev)
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()
plt.plot(lstX, lstY, 'o-r', alpha=0.7, label="first", lw=5, mec='b', mew=2, ms=10)
plt.show()
