import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import math
def generate_data(k=3, n_points=20):
###Генерирует данные для кластеризации
    x = []
    y = []
    labels = []
#Параметры для каждого кластера (центр и радиус)
    cluster_params = [
        ((2, 2), 1),  # Центр (2, 2), радиус 1
        ((7, 7), 2),  # Центр (7, 7), радиус 2
        ((2, 7), 1.5)   # Центр (2, 7), радиус 1.5
    ]
    for i in range(k):
        (center_x, center_y), radius = cluster_params[i]
        for _ in range(n_points):
            # Генерируем случайный угол и расстояние от центра
            angle = np.random.uniform(0, 2 * np.pi)
            distance = np.random.uniform(0, radius)
            # Преобразуем полярные координаты в декартовы
            point_x = center_x + distance * np.cos(angle)
            point_y = center_y + distance * np.sin(angle)
            x.append(point_x)
            y.append(point_y)
            labels.append(i)  # Метка кластера
    return x, y, labels
def initialize_centroids(x, y, k):
    #Инициализирует центроиды случайным образом из набора данных
    indices = np.random.choice(len(x), k, replace=False)
    centroids_x = [x[i] for i in indices]
    centroids_y = [y[i] for i in indices]
    return centroids_x, centroids_y
def assign_to_clusters(x, y, centroids_x, centroids_y):
    #Назначает каждую точку ближайшему центроиду
    labels = []
    for i in range(len(x)):
        distances = [math.sqrt((x[i] - centroids_x[j])**2 + (y[i] - centroids_y[j])**2) for j in range(len(centroids_x))]
        closest_cluster = np.argmin(distances)
        labels.append(closest_cluster)
    return labels
def update_centroids(x, y, labels, k):
    #Обновляет координаты центроидов на основе среднего значения точек в каждом кластере
    new_centroids_x = []
    new_centroids_y = []
    for i in range(k):
        cluster_points_x = [x[j] for j in range(len(x)) if labels[j] == i]
        cluster_points_y = [y[j] for j in range(len(y)) if labels[j] == i]

        if cluster_points_x:  # Проверка, что в кластере есть точки
            new_centroids_x.append(np.mean(cluster_points_x))
            new_centroids_y.append(np.mean(cluster_points_y))
        else:
            # Если кластер пустой, сохраняем старый центроид или выбираем случайную точку
            # В данном случае, сохраняем старый центроид
            new_centroids_x.append(centroids_x[i])
            new_centroids_y.append(centroids_y[i])

    return new_centroids_x, new_centroids_y
def k_means(x, y, k=3, delta_x=0.01, delta_y=0.01, max_iterations=100):
    #Реализация алгоритма k-средних
    centroids_x, centroids_y = initialize_centroids(x, y, k)
    history = []  # Список для хранения истории кластеризации на каждой итерации
    for iteration in range(max_iterations):
        labels = assign_to_clusters(x, y, centroids_x, centroids_y)
        history.append((list(labels), list(centroids_x), list(centroids_y)))  # Сохраняем состояние
        new_centroids_x, new_centroids_y = update_centroids(x, y, labels, k)
        # Проверка условия остановки
        max_dx = max([abs(new_centroids_x[i] - centroids_x[i]) for i in range(k)])
        max_dy = max([abs(new_centroids_y[i] - centroids_y[i]) for i in range(k)])
        if max_dx <= delta_x and max_dy <= delta_y:
            print(f"Алгоритм сошелся на итерации {iteration+1}")
            centroids_x, centroids_y = new_centroids_x, new_centroids_y
            labels = assign_to_clusters(x, y, centroids_x, centroids_y) # Финальное назначение
            history.append((list(labels), list(centroids_x), list(centroids_y))) #Сохраняем финальное состояние
            break
        centroids_x, centroids_y = new_centroids_x, new_centroids_y
    return history
# 1. Генерация данных
x, y, true_labels = generate_data(k=3, n_points=20)
# 2. Запуск k-средних
history = k_means(x, y, k=3)
# 3. Визуализация
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
# Начальное состояние (первая итерация)
initial_labels, initial_centroids_x, initial_centroids_y = history[0]
scatter = ax.scatter(x, y, c=initial_labels, cmap='viridis') # Используем viridis, чтобы цвета были различимы
centroids, = ax.plot(initial_centroids_x, initial_centroids_y, 'ro', markersize=8)
axcolor = 'lightgoldenrodyellow'
ax_iter = fig.add_axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
slider = Slider(ax_iter, 'Итерация', 0, len(history) - 1, valinit=0, valstep=1)
def update(val):
    iteration = int(slider.val)
    labels, centroids_x, centroids_y = history[iteration]
    scatter.set_offsets(np.c_[x, y])
    scatter.set_array(np.array(labels))
    centroids.set_xdata(centroids_x)
    centroids.set_ydata(centroids_y)
    fig.canvas.draw_idle()
slider.on_changed(update)
plt.show()
