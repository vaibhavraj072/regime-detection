# 🧠 Regime Detection in Market Microstructure Data

## 📄 Final Report  
**Authored by:** Vaibhav Raj  
📘 [Click to read the final report](https://docs.google.com/document/d/1qLmr22UbpWiM6WHchLKa2RddSxvw8RUZu5mbb1eTDKk/edit?usp=sharing)

---

## 📝 Problem Statement

This project is based on a real-world task provided by a company. The objective is to analyze order book and trade data, engineer meaningful features, and apply clustering to detect **market regimes**.

📄 **Task Document Provided by @RozReturns**  
🔗 [View the official task description](https://docs.google.com/document/d/1SXLmYQtJEIFHq3ULb2Qejl5in0U9ZwQBFQdXD6RqpX8/edit?tab=t.0)

📦 **Dataset for the Task**  
🔗 [Access the Dataset (Google Drive)](https://drive.google.com/drive/folders/1gFLwPLTE0nUN-MHoOn5u_1yrlbpI3Fst?usp=sharing)

---

## 🧠 What is Regime Detection?

In simple terms, a **regime** refers to a distinct type of market behavior.  
Examples include:
- Calm vs. volatile periods
- Buy-dominant vs. sell-dominant markets
- Stable vs. rapidly changing prices

We identify regimes using **unsupervised learning (KMeans Clustering)** on carefully engineered features.

---

## 🔧 Features Engineered

We processed high-frequency order book (`depth20`) and trade (`aggTrade`) data to compute:

- `spread`: Difference between best ask and best bid
- `imbalance`: Buy/sell pressure in the order book
- `microprice`: Weighted average of bid and ask
- `volatility`: Price fluctuation over time
- `volume_imbalance`: Rolling difference between buy and sell volume

---

## 🤖 Clustering and Output

We used **KMeans clustering** to classify each timestamp into one of several market regimes based on the engineered features.

### Outputs:
- 📄 `merged_with_regimes.csv`: Dataset with regime labels
- 📊 `regime_summary.csv`: Summary of average feature values per regime
- 📈 `regime_timeline.png`: Visualization of regime transitions over time

---

## 📁 Folder Structure

regime-detection/ │ ├── data/ │ ├── aggTrade/ │ └── depth20_1000ms/ │ ├── outputs/ │ ├── clusters/ │ │ ├── merged_with_regimes.csv │ │ └── regime_summary.csv │ └── plots/ │ └── regime_timeline.png │ ├── src/ │ ├── load_data.py │ ├── feature_engineering.py │ ├── clustering.py │ └── visualization.py │ ├── main.py └── README.md
  
---

## 🛠️ How to Run the Project

1. Install Python packages:
   ```bash
   pip install -r requirements.txt
python main.py

2.Check the outputs/ folder for:
Clustered CSVs in outputs/clusters/
Regime timeline plot in outputs/plots/

✅ Project Milestones
 Load & preprocess order book and trade data
 Engineer key features like spread, imbalance, volatility
 Apply clustering to detect market regimes
 Visualize timeline of market behavior shifts
 Generate full report & summaries

 🙋 About the Author
Vaibhav Raj
A Computer Science student with a passion for quantitative analysis, trading systems, and AI.

🌐[Visit my Portfolio](https://vaibhavrajportfolio.vercel.app/)
