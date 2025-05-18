import numpy as np
import matplotlib.pyplot as plt
from sklearn.kernel_ridge import KernelRidge
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
import random

# 1. Генерация сложной нелинейной функции
def f(x):
    return 2*np.sin(1.5*x) + 0.5*np.exp(-0.2*x)*np.cos(5*x) + 0.3*x

# 2. Настройка методов регрессии
models = [
    ("Kernel Ridge (RBF)", 
     GridSearchCV(
         KernelRidge(kernel='rbf'),
         param_grid={"alpha": [1e0, 0.1, 1e-2], 
                    "gamma": np.logspace(-2, 2, 5)},
         cv=5)),
    ("Метод опорных векторов", 
     SVR(kernel='rbf', C=10, gamma=0.5, epsilon=0.1)),
    ("Случайный лес", 
     RandomForestRegressor(n_estimators=150, max_depth=5, random_state=42))
]

# 3. Генерация данных с неоднородным шумом
x_min, x_max = 0, 8
x = np.linspace(x_min, x_max, 200).reshape(-1, 1)
y_true = f(x).ravel()

np.random.seed(42)
noise = 0.3 * np.random.normal(0, 1, size=len(x)) * (1 + np.sin(x.ravel()))
y = y_true + noise

# 4. Обучение и визуализация
plt.figure(figsize=(20, 6))
plt.suptitle("Сравнение методов нелинейной регрессии", fontsize=16, y=1.05)

for i, (name, model) in enumerate(models):
    # Обучение с подбором параметров для Kernel Ridge
    if name.startswith("Kernel Ridge"):
        model.fit(x, y)
        best_params = model.best_params_
        model = model.best_estimator_
    else:
        model.fit(x, y)
    
    y_pred = model.predict(x)
    
    # Метрики
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    mae = np.mean(np.abs(y_true - y_pred))
    
    # График
    ax = plt.subplot(1, 3, i+1)
    
    # Отображение подобранных параметров для Kernel Ridge
    title = f"{name}\nMSE: {mse:.4f} | R²: {r2:.4f}"
    if name.startswith("Kernel Ridge"):
        title += f"\nalpha: {best_params['alpha']:.3f}, gamma: {best_params['gamma']:.3f}"
    
    ax.set_title(title)
    ax.scatter(x, y, color='blue', alpha=0.5, label='Данные с шумом')
    ax.plot(x, y_true, 'g-', linewidth=3, label='Истинная функция')
    ax.plot(x, y_pred, 'r-', linewidth=2.5, label='Предсказание')
    
    # Особое оформление для Kernel Ridge
    if name.startswith("Kernel Ridge"):
        ax.fill_between(x.ravel(), 
                       y_pred - 0.3, 
                       y_pred + 0.3,
                       alpha=0.1, 
                       color='red')
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

