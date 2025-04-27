"""
import random
a = random.sample(range(1, 12), 3)
print(a)
11 6 8 
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering, DBSCAN, HDBSCAN, estimate_bandwidth, MeanShift
from sklearn import mixture
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs, make_moons, make_circles
# Функции генерации данных
def generate_noisy_circles():
    return make_circles(n_samples=300, factor=0.5, noise=0.05)

def generate_noisy_moons():
    return make_moons(n_samples=300, noise=0.05)

def generate_blobs_with_variance():
    return make_blobs(n_samples=300, cluster_std=[1.0, 2.5, 0.5], random_state=170)

def generate_anisotropic():
    X, y = make_blobs(n_samples=300, random_state=170)
    transformation = [[0.6, -0.6], [-0.4, 0.8]]
    X = np.dot(X, transformation)
    return X, y

def generate_uniform():
    return np.random.rand(300, 2), None

def generate_structured_blobs():
    X, y = make_blobs(n_samples=300, random_state=170)
    X_filtered = np.vstack((X[y == 0][:30], X[y == 1][:100], X[y == 2][:10]))
    y_filtered = np.concatenate((np.zeros(30), np.ones(100), np.ones(10)*2))
    return X_filtered, y_filtered

# Алгоритмы кластеризации
def agglomerative_clustering(X, n_clusters=2):
    clustering = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward')
    return clustering.fit_predict(X)

def gaussian_mixture(X, n_components=2):
    gmm = mixture.GaussianMixture(n_components=n_components, covariance_type='full')
    gmm.fit(X)
    return gmm.predict(X)

def hdbscan_clustering(X, min_cluster_size=5):
    clusterer = HDBSCAN(min_cluster_size=min_cluster_size)
    return clusterer.fit_predict(X)


def plot_clusters(X, labels, title):
    plt.scatter(X[:, 0], X[:, 1], c=labels)
    plt.title(title)
    plt.show()

#Методы кластеризации с данными
X, y = generate_noisy_circles()
X = StandardScaler().fit_transform(X) 

labels_agg = agglomerative_clustering(X, n_clusters=2)
plot_clusters(X, labels_agg, "Agglomerative Clustering on noisy_circles")

labels_gmm = gaussian_mixture(X, n_components=2)
plot_clusters(X, labels_gmm, "Gaussian Mixture on noisy_circles")

labels_hdbscan = hdbscan_clustering(X, min_cluster_size=5)
plot_clusters(X, labels_hdbscan, "HDBSCAN on noisy_circles")
X, y =  generate_noisy_moons()
X = StandardScaler().fit_transform(X) 

labels_agg = agglomerative_clustering(X, n_clusters=2)
plot_clusters(X, labels_agg, "Agglomerative Clustering on noisy_moons")

labels_gmm = gaussian_mixture(X, n_components=2)
plot_clusters(X, labels_gmm, "Gaussian Mixture on noisy_moons ")

labels_hdbscan = hdbscan_clustering(X, min_cluster_size=5)
plot_clusters(X, labels_hdbscan, "HDBSCAN on noisy_moons")
X, y = generate_blobs_with_variance()
X = StandardScaler().fit_transform(X) 

labels_agg = agglomerative_clustering(X, n_clusters=2)
plot_clusters(X, labels_agg, "Agglomerative Clustering on blobs_with_variance")

labels_gmm = gaussian_mixture(X, n_components=2)
plot_clusters(X, labels_gmm, "Gaussian Mixture on blobs_with_variance")

labels_hdbscan = hdbscan_clustering(X, min_cluster_size=5)
plot_clusters(X, labels_hdbscan, "HDBSCAN on blobs_with_variance")
X, y = generate_anisotropic()
X = StandardScaler().fit_transform(X)

labels_agg = agglomerative_clustering(X, n_clusters=2)
plot_clusters(X, labels_agg, "Agglomerative Clustering on anisotropic")

labels_gmm = gaussian_mixture(X, n_components=2)
plot_clusters(X, labels_gmm, "Gaussian Mixture on anisotropic")

labels_hdbscan = hdbscan_clustering(X, min_cluster_size=5)
plot_clusters(X, labels_hdbscan, "HDBSCAN on anisotropic")
X, y =generate_uniform()
X = StandardScaler().fit_transform(X)
labels_agg = agglomerative_clustering(X, n_clusters=2)
plot_clusters(X, labels_agg, "Agglomerative Clustering on uniform")

labels_gmm = gaussian_mixture(X, n_components=2)
plot_clusters(X, labels_gmm, "Gaussian Mixture on uniform")

labels_hdbscan = hdbscan_clustering(X, min_cluster_size=5)
plot_clusters(X, labels_hdbscan, "HDBSCAN on uniform")
X, y =generate_structured_blobs()
X = StandardScaler().fit_transform(X)

labels_agg = agglomerative_clustering(X, n_clusters=2)
plot_clusters(X, labels_agg, "Agglomerative Clustering on structured_blobs")

labels_gmm = gaussian_mixture(X, n_components=2)
plot_clusters(X, labels_gmm, "Gaussian Mixture on structured_blobs")

labels_hdbscan = hdbscan_clustering(X, min_cluster_size=5)
plot_clusters(X, labels_hdbscan, "HDBSCAN on structured_blobs")
