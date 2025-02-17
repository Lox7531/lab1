import matplotlib.pyplot as plt
import numpy as np
'''
import random
random.seed(4)
task1=random.randint(1,24)
print(task1)
'''
print("Введите a")
a=int(input())
print("Введите b")
b=int(input())
print("Введите c")
c=int(input())
print("Введите начало диапазона")
x1=int(input())
print("Введите конец диапазона")
x2=int(input())
plt.style.use('_mpl-gallery')
x = np.linspace(x1, x2, 100)
y = a*x**2 + b * x + c
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=2.0)
ax.set(xlim=(x1, x2), xticks=np.arange(1+x1, x2),
       ylim=(x1, x2), yticks=np.arange(1+x1, x2))
plt.show()