import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------- Data Loading ----------
@st.cache_data
def load_data():
    feat = pd.read_csv("D:\\Python_Training\\Trade-behavior\\outputs\\trader_features_by_day.csv", parse_dates=['date'])
    sentiment_summary = pd.read_csv("D:\\Python_Training\\Trade-behavior\\outputs\\features_by_sentiment.csv")
    return feat, sentiment_summary

feat, sentiment_summary = load_data()

# ---------- Layout ----------
st.title("Trader Performance vs Market Sentiment")
st.markdown(
    """
    Analyze how trader metrics (PnL, win rates, trade count, etc.) vary across Bitcoin market sentiment states.
    """
)

# ---------- Sentiment Selection ----------
sentiments = feat['classification'].unique()
selected_sentiment = st.selectbox("Choose sentiment class for detail exploration", sorted(sentiments))

# ---------- Main KPIs for Chosen Sentiment ----------
st.header(f"Summary Metrics: {selected_sentiment}")
sent_kpi = sentiment_summary[sentiment_summary['classification'] == selected_sentiment]
st.dataframe(sent_kpi)

# ---------- Distribution Plot ----------
st.subheader("PnL Distribution by Sentiment")
fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(data=feat, x="classification", y="daily_pnl", ax=ax)
ax.set_title("Distribution of Daily PnL by Sentiment")
st.pyplot(fig)

# ---------- Line Chart: PnL Over Time ----------
st.subheader(f"PnL Over Time: Accounts in {selected_sentiment}")
accounts = feat[feat['classification'] == selected_sentiment]['Account'].unique()
selected_accounts = st.multiselect("Filter accounts", accounts, default=accounts[:3])

if selected_accounts:
    for acct in selected_accounts:
        data = feat[(feat['Account']==acct) & (feat['classification']==selected_sentiment)]
        st.line_chart(data.set_index('date')['daily_pnl'], height=200, width=600)

# ---------- Rolling Average Plot ----------
st.subheader("7-Day Rolling Mean of PnL (All Accounts)")
ROLLING_WINDOW = 7
pivot = feat.pivot_table('daily_pnl', index='date', columns='classification', aggfunc='mean')
rolling = pivot.rolling(ROLLING_WINDOW).mean()
st.line_chart(rolling)

# ---------- Win-Rate Plot ----------
st.subheader("Win Rate by Sentiment")
fig2, ax2 = plt.subplots(figsize=(8,4))
sns.barplot(data=sentiment_summary, x='classification', y='mean_win_rate', ax=ax2)
ax2.set_title('Average Win Rate per Sentiment')
st.pyplot(fig2)

# ---------- Download Section ----------
st.subheader("Download Data")
st.download_button("Download Account-Day features (.csv)", feat.to_csv(index=False), file_name='trader_features_by_day.csv')
st.download_button("Download Sentiment summary (.csv)", sentiment_summary.to_csv(index=False), file_name='features_by_sentiment.csv')
st.download_button("Download Merged Dataset (.csv)", sentiment_summary.to_csv(index=False), file_name='final_merged_trades.csv')

# ---------- Advanced Filtering ----------
st.subheader("Advanced Table Filtering")
with st.expander("Show filterable data table"):
    col1, col2 = st.columns(2)
    min_trades = col1.number_input("Min daily trades", min_value=1, value=5)
    max_trades = col2.number_input("Max daily trades", min_value=1, value=1000)
    filtered = feat[(feat['trade_count']>=min_trades)&(feat['trade_count']<=max_trades)]
    st.dataframe(filtered)

st.markdown("— Powered by Streamlit. Built by Deepshikha.")
