import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

def prepare_features_for_clustering(df, feature_cols):
    """
    Normalize selected feature columns using StandardScaler
    """
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df[feature_cols].fillna(0))
    return scaled_features

def apply_kmeans(features, n_clusters=4):
    """
    Apply KMeans clustering on the given feature matrix
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(features)
    return labels, kmeans

def evaluate_clustering(features, labels):
    """
    Evaluate using Silhouette Score
    """
    score = silhouette_score(features, labels)
    return score
