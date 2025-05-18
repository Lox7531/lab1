import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
plt.style.use('seaborn-v0_8')
plt.figure(figsize=(18, 25))
plt.suptitle("Сравнение методов классификации", y=1.02, fontsize=16, fontweight='bold')
models = [
    ("K-ближайших соседей (k=3)", KNeighborsClassifier(n_neighbors=3)),
    ("Метод опорных векторов (RBF)", SVC(kernel='rbf', C=1.0, probability=True)),
    ("Дерево решений (max_depth=5)", DecisionTreeClassifier(max_depth=5, criterion='entropy', random_state=42))
]
datasets_info = [
    ("Две окружности", datasets.make_circles(n_samples=500, factor=0.5, noise=0.05, random_state=30)),
    ("Две параболы", datasets.make_moons(n_samples=500, noise=0.05, random_state=30)),
    ("Кластеры с разной дисперсией", datasets.make_blobs(n_samples=500, cluster_std=[1.0, 0.5], random_state=30, centers=2)),
    ("Анизотропные данные", (np.dot(datasets.make_blobs(n_samples=500, random_state=170, centers=2)[0], 
                             [[0.6, -0.6], [-0.4, 0.8]]), 
                          datasets.make_blobs(n_samples=500, random_state=170, centers=2)[1])),
    ("Слабо разделимые данные", datasets.make_blobs(n_samples=500, random_state=30, centers=2))
]
train_cmap = plt.cm.coolwarm
test_cmap = plt.cm.coolwarm
for row, (ds_name, (X, y)) in enumerate(datasets_info):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                         np.linspace(y_min, y_max, 200))
    grid = np.c_[xx.ravel(), yy.ravel()]
    for col, (model_name, model) in enumerate(models):
        ax = plt.subplot(5, 3, row * 3 + col + 1)
        model.fit(X_train, y_train)
        if hasattr(model, "predict_proba"):
            Z = model.predict_proba(grid)[:, 1].reshape(xx.shape)
        else:
            Z = model.predict(grid).reshape(xx.shape)
        y_pred = model.predict(X_test)
        accuracy = np.mean(y_test == y_pred)
        plt.contourf(xx, yy, Z, alpha=0.3, levels=20, cmap='RdBu')
        plt.contour(xx, yy, Z, levels=[0.5], colors='black', linewidths=2)
        plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, 
                   cmap=train_cmap, alpha=0.8, edgecolors='k', 
                   s=40, label='Обучающие')
        correct = y_test == y_pred
        plt.scatter(X_test[correct, 0], X_test[correct, 1], 
                   c=y_test[correct], cmap=test_cmap, 
                   marker='o', s=60, edgecolors='k', linewidth=1.5,
                   label='Правильные')
        plt.scatter(X_test[~correct, 0], X_test[~correct, 1], 
                   c=y_test[~correct], cmap=test_cmap, 
                   marker='x', s=80, linewidth=2.5,
                   label='Ошибки')
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.xticks([])
        plt.yticks([])
        if row == 0:
            plt.title(model_name, fontsize=12, pad=12)
        if col == 0:
            plt.ylabel(f"{ds_name}\nAccuracy: {accuracy:.3f}", 
                      fontsize=10, labelpad=10)
        else:
            plt.ylabel(f"Accuracy: {accuracy:.3f}", fontsize=10, labelpad=10)
        if row == 0 and col == 0:
            plt.legend(bbox_to_anchor=(0., 1.02, 3., .102), loc='lower left',
                      ncol=3, mode="expand", borderaxespad=0., fontsize=10)

plt.tight_layout()
plt.subplots_adjust(top=0.92, hspace=0.3, wspace=0.1)
plt.show()
