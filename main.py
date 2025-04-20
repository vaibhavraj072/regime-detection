from src.load_data import load_agg_trade, load_depth20, list_files_in_folder

# Path to your data
agg_folder = "data/aggTrade"
depth_folder = "data/depth20_1000ms"

# Get list of files
agg_files = list_files_in_folder(agg_folder)
depth_files = list_files_in_folder(depth_folder)

# Load sample file
agg_df = load_agg_trade(agg_files[0])
depth_df = load_depth20(depth_files[0])

# Print sample rows
print("AggTrade sample:\n", agg_df.head())
print("\nDepth20 sample:\n", depth_df.head())
print("agg_files:", agg_files)
