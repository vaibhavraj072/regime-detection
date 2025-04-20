# EXISTING aggTrade logic
from src.load_data import load_agg_trade, list_files_in_folder

agg_files = list_files_in_folder("data/aggTrade")
agg_df = load_agg_trade(agg_files[0])
print("AggTrade sample:\n", agg_df.head())

# NEW depth20 + features
from src.load_data import load_depth20
from src.feature_engineering import add_depth_features

depth_files = list_files_in_folder("data/depth20_1000ms")
depth_df = load_depth20(depth_files[0])
depth_df = add_depth_features(depth_df)

from src.feature_engineering import add_advanced_depth_features

depth_df = add_advanced_depth_features(depth_df)

print(depth_df[['Time', 'cum_bid_qty', 'cum_ask_qty', 'midprice', 'mid_return', 'volatility']].head(15))

print(depth_df[['Time', 'BidPriceL1', 'AskPriceL1', 'spread', 'imbalance', 'microprice']].head())

from src.feature_engineering import compute_volume_features

agg_df = compute_volume_features(agg_df, window='10s')

print(agg_df[['Time', 'Price', 'Quantity', 'buy_vol_rolling', 'sell_vol_rolling', 'volume_imbalance']].head(15))


from src.feature_engineering import merge_orderbook_trades

# Merge both DataFrames
merged_df = merge_orderbook_trades(depth_df, agg_df)

# See what we've got!
print(merged_df[['Time', 'spread', 'imbalance', 'microprice', 'volume_imbalance', 'volatility']].head(10))


from src.clustering import prepare_features_for_clustering, apply_kmeans, evaluate_clustering

# Select features to cluster on
feature_cols = ['spread', 'imbalance', 'microprice', 'volatility', 'volume_imbalance']
features = prepare_features_for_clustering(merged_df, feature_cols)

# Apply KMeans clustering
labels, kmeans = apply_kmeans(features, n_clusters=4)

# Save cluster labels
merged_df['regime'] = labels

# Evaluate clustering
score = evaluate_clustering(features, labels)
print(f"Silhouette Score: {score:.4f}")

# See sample with regime labels
print(merged_df[['Time'] + feature_cols + ['regime']].head(15))


from src.visualization import plot_regime_timeline

plot_regime_timeline(merged_df)
plot_regime_timeline(merged_df, save=True)

