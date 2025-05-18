import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.datasets import make_blobs, make_moons, make_circles
from sklearn.preprocessing import StandardScaler

ALGORITHMS = {
    'K-Means': KMeans,
    'DBSCAN': DBSCAN,
    'Agglomerative': AgglomerativeClustering
}

PARAMS = {
    'K-Means': {'n_clusters': 3},
    'DBSCAN': {'eps': 0.3, 'min_samples': 10},
    'Agglomerative': {'n_clusters': 3, 'linkage': 'ward'}
}

# Функции для генерации данных
def generate_blobs():
    X, _ = make_blobs(n_samples=300, centers=3, cluster_std=0.8, random_state=0)
    return X

def generate_moons():
    X, _ = make_moons(n_samples=300, noise=0.05, random_state=0)
    return X

def generate_circles():
    X, _ = make_circles(n_samples=300, factor=0.5, noise=0.05, random_state=0)
    return X

def generate_aniso():
    X, _ = make_blobs(n_samples=300, centers=3, random_state=0)
    transformation = [[0.6, -0.6], [-0.4, 0.8]]
    X = np.dot(X, transformation)
    return X

def generate_varied():
    X, _ = make_blobs(n_samples=300, centers=3, cluster_std=[1.0, 2.5, 0.5], random_state=0)
    return X

def generate_noisy():
    X, _ = make_blobs(n_samples=100, centers=3, random_state=0)
    noise = np.random.uniform(low=-10, high=10, size=(20, 2))
    return np.vstack([X, noise])

# Список всех генераторов
GENERATORS = [
    ('Blobs', generate_blobs),
    ('Moons', generate_moons),
    ('Circles', generate_circles),
    ('Anisotropic', generate_aniso),
    ('Varied Variance', generate_varied),
    ('Noisy', generate_noisy)
]

# Функция для кластеризации
def apply_clustering(algorithm, params, X):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    model = algorithm(**params)
    if algorithm == DBSCAN:
        labels = model.fit_predict(X_scaled)
    else:
        labels = model.fit_predict(X_scaled)
    
    return labels

# Визуализация результатов
def plot_results(generators, algorithms):
    plt.figure(figsize=(20, 16))
    plt.subplots_adjust(hspace=0.4, wspace=0.2)
    
    for i, (name, generator) in enumerate(generators):
        X = generator()
        
        for j, (alg_name, algorithm) in enumerate(algorithms.items()):
            ax = plt.subplot(len(generators), len(algorithms), i*len(algorithms) + j + 1)
            
            labels = apply_clustering(algorithm, PARAMS[alg_name], X)
            
            ax.scatter(X[:, 0], X[:, 1], c=labels, s=10, cmap='viridis')
            ax.set_title(f"{name}\n{alg_name}")
            ax.set_xticks([])
            ax.set_yticks([])
    
    plt.show()

# Запуск визуализации
plot_results(GENERATORS, ALGORITHMS)

