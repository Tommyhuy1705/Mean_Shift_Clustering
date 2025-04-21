# mean_shift_utils.py

import numpy as np
from sklearn.cluster import MeanShift
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from sklearn.preprocessing import StandardScaler

def evaluate_mean_shift(X_scaled, bandwidths):
    models = []
    silhouette_scores = []
    db_scores = []
    ch_scores = []
    n_clusters_list = []

    for bw in bandwidths:
        model = MeanShift(bandwidth=bw, bin_seeding=True)
        model.fit(X_scaled)
        labels = model.labels_
        n_clusters = len(np.unique(labels))

        models.append((model, labels, n_clusters))
        n_clusters_list.append(n_clusters)

        if n_clusters > 1:
            silhouette_scores.append(silhouette_score(X_scaled, labels))
            db_scores.append(davies_bouldin_score(X_scaled, labels))
            ch_scores.append(calinski_harabasz_score(X_scaled, labels))
        else:
            silhouette_scores.append(np.nan)
            db_scores.append(np.nan)
            ch_scores.append(np.nan)

    return models, silhouette_scores, db_scores, ch_scores, n_clusters_list
