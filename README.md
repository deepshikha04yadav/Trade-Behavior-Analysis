# Trade-Behavior-Analysis

Explore the relationship between crypto market sentiment and trader performance on Hyperliquid.

## 📊 Project Overview
Trade-Behavior-Analysis investigates how Bitcoin market sentiment ("Fear" vs "Greed") influences trader outcomes. By combining market sentiment data with detailed historical trading records, this project discovers performance patterns, risk profiles, and actionable behaviors that can drive smarter trading strategies.

Core tasks:

* Merge and clean trading and sentiment datasets

* Engineer robust features per trader and sentiment regime

* Visualize and statistically analyze performance behaviors

* Equip analysts with an interactive Streamlit dashboard

## 📁 Repository Structure
```
├── data/                # Raw input data (CSV files: trader, sentiment)
├── notebooks/           # Jupyter notebooks (data prep, EDA, analysis)
├── outputs/             # Exports: engineered features, results
├── dashboard.py         # Streamlit dashboard app
├── README.md            # Project overview 
└── .gitattributes
```
## 🚀 Getting Started
### 1. Clone the repository
```
git clone https://github.com/deepshikha04yadav/Trade-Behavior-Analysis.git
cd Trade-Behavior-Analysis
```
### 2. Install dependencies
We recommend using a virtual environment.
```
pip install -r requirements.txt
# If requirements.txt does not exist, install these:
pip install pandas matplotlib seaborn streamlit scikit-learn
```
### 3. Prepare data
Add your trading and fear/greed index CSV files to the data/ directory.

* Example source:

  * Trader Data: historical_trader_data.csv
  * Sentiment Data: fear_greed_index.csv

### 4. Run exploratory analysis
Jupyter notebooks in notebooks/ walk through data preparation, feature engineering, and initial visualizations.
```
jupyter notebook
```
### 5. Launch interactive dashboard
```
streamlit run dashboard.py
```
Explore trader PnL by sentiment, download tables, and visualize trends interactively.

## 🔑 Features
* Automated Data Merging & Cleaning: All records synchronized by date and sentiment state.

* Feature Engineering: Daily and sentiment-based metrics—PnL, win rate, trade count, risk indicators.

* Exploratory Analysis: Notebooks for statistical testing and in-depth behavioral discovery.

* Streamlit Dashboard: Interactive charts, summary KPIs, table explorer, and export tools.

* Customizable Pipeline: Adaptable for new data or exchange sources as needed.

## 📷 Dashboard Preview
<img width="1277" height="629" alt="image" src="https://github.com/user-attachments/assets/cc17cf10-aeb6-4c7e-ad94-3c80697cf700" />
<img width="1276" height="771" alt="image" src="https://github.com/user-attachments/assets/84ea92ea-75a1-4fcf-bf5e-ff3f180f26c2" />
<img width="1187" height="804" alt="image" src="https://github.com/user-attachments/assets/78a42ddd-dcfd-48bb-b05f-8aaf5a94f6bd" />


## 📝 How to Contribute
Pull requests are welcome! Please open an issue first to discuss new features or fixes.
