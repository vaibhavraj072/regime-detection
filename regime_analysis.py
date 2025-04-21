import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# === Load Data ===
csv_path = r"C:\Users\vaibh\OneDrive\Documents\GitHub\regime-detection\outputs\clusters\merged_with_regimes.csv"
df = pd.read_csv(csv_path)

# === Ensure plot output directory exists ===
plot_dir = r"C:\Users\vaibh\OneDrive\Documents\GitHub\regime-detection\outputs\plots"
os.makedirs(plot_dir, exist_ok=True)

# === Features to Analyze ===
features = ['spread', 'imbalance', 'microprice', 'volatility', 'volume_imbalance']

# === Plot Distributions and Boxplots ===
for feature in features:
    # KDE Plot
    plt.figure(figsize=(10, 5))
    sns.kdeplot(data=df, x=feature, hue='regime', common_norm=False, fill=True, alpha=0.4)
    plt.title(f"{feature} Distribution by Regime")
    plt.grid(True)
    plt.tight_layout()
    kde_path = os.path.join(plot_dir, f"{feature}_kde_by_regime.png")
    plt.savefig(kde_path)
    print(f"📊 Saved KDE plot: {kde_path}")
    plt.close()

    # Box Plot
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x='regime', y=feature, palette='Set2')
    plt.title(f"{feature} by Regime")
    plt.grid(True)
    plt.tight_layout()
    box_path = os.path.join(plot_dir, f"{feature}_box_by_regime.png")
    plt.savefig(box_path)
    print(f"📦 Saved boxplot: {box_path}")
    plt.close()

print("\n✅ All regime analysis plots generated successfully.")
