def plot_regime_timeline(df, time_col='Time', regime_col='regime', save=False):
    import matplotlib.pyplot as plt
    import os

    plt.figure(figsize=(15, 5))

    # Fixed: valid color
    plt.plot(df[time_col], df[regime_col], drawstyle='steps-post', color='C0', alpha=0.8)

    plt.title("Market Regime Over Time")
    plt.xlabel("Time")
    plt.ylabel("Regime")
    plt.grid(True)
    plt.tight_layout()

    if save:
        os.makedirs(r"C:\Users\vaibh\OneDrive\Documents\GitHub\regime-detection\outputs\plots", exist_ok=True)
        plt.savefig(r"C:\Users\vaibh\OneDrive\Documents\GitHub\regime-detection\outputs\plots\regime_timeline.png")
        print("✅ Regime plot saved to: outputs/plots/regime_timeline.png")

    plt.show()
