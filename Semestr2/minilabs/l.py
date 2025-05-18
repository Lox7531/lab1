import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """Исходная функция: x^4 - 3x^3 + 2"""
    return x**4 - 3*x**3 + 2

def df(x):
    """Производная функции: 4x^3 - 9x^2"""
    return 4*x**3 - 9*x**2

true_min_x = 2.25
true_min_y = f(true_min_x)
def gradientDescend(func=lambda x: x**2, 
                   diffFunc=lambda x: 2*x, 
                   x0=3, 
                   speed=0.01, 
                   epochs=100):
    xList = []
    yList = []
    x = x0
    for _ in range(epochs):
        x = x - speed * diffFunc(x)
        xList.append(x)
        yList.append(func(x))
    return xList, yList

def plot_gradient_descent(xList, yList, func, true_min):
    x_vals = np.linspace(min(xList + [true_min[0]]) - 1, 
                       max(xList + [true_min[0]]) + 1, 
                       400)
    y_vals = func(x_vals)
    plt.figure(figsize=(12, 7))
    plt.plot(x_vals, y_vals, 'b-', linewidth=2, label='Функция: $x^4 - 3x^3 + 2$')
    plt.scatter(xList, yList, c='r', s=50, label='Точки градиентного спуска')
    plt.scatter([true_min[0]], [true_min[1]], c='g', marker='*', s=300, label='Истинный минимум')
    plt.scatter([xList[0]], [yList[0]], c='k', marker='o', s=100, label='Начальная точка')
    plt.scatter([xList[-1]], [yList[-1]], c='m', marker='X', s=100, label='Конечная точка')
    plt.title('Метод градиентного спуска', fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('f(x)', fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True)
    for i in range(len(xList)-1):
        plt.annotate('', xy=(xList[i+1], yList[i+1]), 
                    xytext=(xList[i], yList[i]),
                    arrowprops=dict(arrowstyle='->', color='gray', lw=1, ls='--'))
    
    plt.show()
xList, yList = gradientDescend(func=f, diffFunc=df, x0=3, speed=0.001, epochs=100)
plot_gradient_descent(xList, yList, f, (true_min_x, true_min_y))


