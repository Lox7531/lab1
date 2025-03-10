# y=a*x**2+b*x+c
import matplotlib.pyplot as plt
import numpy as np

#Для самостоятельного ввода
a = int(input('Введите коэффициент a: '))
b = int(input('Введите коэффициент b: '))
c = int(input('Введите коэффициент c: '))
x1 = int(input('Введите начало диапозона: '))
x2 = int(input('Введите конец диапозона: '))

"""
a=1
b=2
c=1
x1=-5
x2=5
"""
x = np.linspace(x1, x2, 50)
y = a*x**2+b*x+c
fig,ax=plt.subplots()
ax.plot(x,y)

plt.xlabel('x')
plt.ylabel('y')
plt.title('y=a*x**2+b*x+c')
plt.show()
