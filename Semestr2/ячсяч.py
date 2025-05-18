import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import random

# Генерация исходных данных
x_min = -10
x_max = 10
points = 50

# Истинная функция (линейная)
true_k = 2.5
true_b = -1.5

x = np.linspace(x_min, x_max, points)
y_true = true_k * x + true_b
y = y_true + np.random.uniform(-3, 3, size=points)  # Добавляем шум

# Функции для вычисления частных производных
def get_dk(x: list, y: list, k: float, b: float) -> float:
    n = len(x)
    total = 0
    for xi, yi in zip(x, y):
        total += xi * ((k * xi + b) - yi)
    result = (2/n) * total
    return result

def get_db(x: list, y: list, k: float, b: float) -> float:
    n = len(x)
    total = 0
    for xi, yi in zip(x, y):
        total += ((k * xi + b) - yi)
    result = (2/n) * total
    return result

# Функция MSE
def mse(x, y, k, b):
    n = len(x)
    total = 0
    for xi, yi in zip(x, y):
        total += ((k * xi + b) - yi) ** 2
    return total / n

# Инициализация параметров для градиентного спуска
speed = 0.001  # Скорость обучения
epochs = 1000    # Количество итераций
k0 = 0          # Начальное значение k
b0 = 0          # Начальное значение b

# Реализация градиентного спуска
def fit(x, y, speed, epochs, k0, b0):
    k = k0
    b = b0
    k_list = [k]
    b_list = [b]
    mse_list = [mse(x, y, k, b)]
    
    for i in range(epochs):
        dk = get_dk(x, y, k, b)
        db = get_db(x, y, k, b)
        
        k = k - speed * dk
        b = b - speed * db
        
        k_list.append(k)
        b_list.append(b)
        mse_list.append(mse(x, y, k, b))
    
    return k_list, b_list, mse_list

# Обучение модели
k_list, b_list, mse_list = fit(x, y, speed, epochs, k0, b0)

# Визуализация результатов
fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.25)

# График данных и линии регрессии
scatter = ax.scatter(x, y, color='blue', label='Исходные данные')
true_line, = ax.plot(x, y_true, 'g-', linewidth=2, label='Истинная функция')
pred_line, = ax.plot(x, k_list[0]*x + b_list[0], 'r-', linewidth=2, label='Предсказание')
ax.set_xlim(x_min, x_max)
ax.set_ylim(min(y)-2, max(y)+2)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)
ax.set_title('Линейная регрессия с градиентным спуском')

# Создание слайдера
ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
slider = Slider(ax_slider, 'Эпоха', 0, epochs, valinit=0, valstep=1)

# Функция обновления графика при изменении слайдера
def update(val):
    epoch = int(slider.val)
    k = k_list[epoch]
    b = b_list[epoch]
    
    pred_line.set_ydata(k*x + b)
    ax.set_title(f'Линейная регрессия (эпоха {epoch}), MSE: {mse_list[epoch]:.2f}')
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()


