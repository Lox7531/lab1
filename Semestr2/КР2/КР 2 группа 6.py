import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor
from matplotlib.widgets import Slider
import pandas as pd

# Генерация данных
x = np.linspace(-10, 10, 200)
y_true = 10 / (1 + np.exp(-0.7 * x + 2))
noise = np.random.poisson(0.5 * y_true) - 0.5 * y_true
y = y_true + noise

# Сохранение данных в файл
data = pd.DataFrame({'x': x, 'y_true': y_true, 'y_noisy': y})
data.to_csv('data.csv', index=False)
print("Данные сохранены в файл 'data.csv'")

# Обучение модели
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

predictions = []
for i in range(1, 101):
    model.set_params(n_estimators=i)
    model.fit(x.reshape(-1, 1), y)
    predictions.append(model.predict(x.reshape(-1, 1)))

# Построение графиков
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
plt.subplots_adjust(bottom=0.2)

# График данных и предсказаний
ax1.plot(x, y_true, 'k--', label='Истинная функция')
ax1.scatter(x, y, color='blue', alpha=0.3, label='Данные с шумом')
pred_line, = ax1.plot(x, predictions[-1], 'r-', label='Предсказание')
ax1.set_title('Градиентный бустинг: приближение функции')
ax1.legend()
ax1.grid(True)

# График ошибки
errors = [np.mean(np.abs(pred - y_true)) for pred in predictions]
ax2.plot(range(1, 101), errors, 'b-')
ax2.set_title('Ошибка (MAE) на каждой итерации')
ax2.set_xlabel('Количество деревьев')
ax2.grid(True)

# Слайдер
ax_slider = plt.axes([0.2, 0.05, 0.6, 0.03])
slider = Slider(ax_slider, 'Итерация', 1, 100, valinit=100, valstep=1)

def update(val):
    i = int(val) - 1
    pred_line.set_ydata(predictions[i])
    fig.canvas.draw_idle()

slider.on_changed(update)
plt.show()
