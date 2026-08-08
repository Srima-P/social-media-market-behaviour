import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------


st.set_page_config(
    page_title="Social Media & Market Dynamics Dashboard",
    layout="wide"
)


# --------------------------------------------------
# DATA LOADING
# --------------------------------------------------


@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    df["date"] = pd.to_datetime(df["date"])
    return df


# --------------------------------------------------
# LOAD DATASETS
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

gme = load_data(BASE_DIR / "final_gme_dataset.csv")
amc = load_data(BASE_DIR / "final_amc_dataset.csv")
tsla = load_data(BASE_DIR / "final_tsla_dataset.csv")
# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------


st.sidebar.title("Dashboard Controls")


stock = st.sidebar.selectbox(
    "Select Stock",
    ["GME", "AMC", "TSLA"]
)


if stock == "GME":
    df = gme
elif stock == "AMC":
    df = amc
else:
    df = tsla
# ==================================================
# RELATIONSHIP ANALYSIS
# ==================================================

st.header("🔗 Relationship Analysis")
st.subheader("ISV vs Volatility")

fig = px.scatter(
    df,
    x="isv",
    y="volatility",
    trendline="ols",
    title="Investor Sentiment Variance vs Volatility"
)
st.plotly_chart(fig, width="stretch")
st.info("""
Hypothesis:
Higher investor disagreement should increase volatility.

Phase 6 Result:
No statistically significant relationship was found.
""")
st.subheader("Discussion Volume vs Volatility")

fig = px.scatter(
    df,
    x="volume",
    y="volatility",
    trendline="ols",
    title="Discussion Volume vs Volatility"
)
st.plotly_chart(fig, width="stretch")
st.success("""
Discussion Volume showed the strongest positive relationship
with volatility among all social-media variables.
""")
st.subheader("Average Sentiment vs Daily Return")

fig = px.scatter(
    df,
    x="avg_sentiment",
    y="daily_return",
    trendline="ols",
    title="Average Sentiment vs Daily Return"
)
st.plotly_chart(fig, width="stretch")
st.info("""
Average sentiment did not significantly predict stock returns.
""")
st.subheader("Sentiment Velocity vs Volatility")

fig = px.scatter(
    df,
    x="sentiment_velocity",
    y="volatility",
    trendline="ols",
    title="Sentiment Velocity vs Volatility"
)

st.plotly_chart(fig, width="stretch")
corr_cols = [
    "volume",
    "avg_sentiment",
    "isv",
    "sentiment_velocity",
    "daily_return",
    "volatility",
    "abnormal_volume"
]

corr_matrix = df[corr_cols].corr()
st.subheader("Correlation Heatmap")

fig = px.imshow(
    corr_matrix,
    text_auto=True,
    aspect="auto",
    title="Correlation Matrix"
)
st.plotly_chart(fig, width="stretch")
st.subheader("Key Correlation Indicators")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Volume ↔ Volatility",
        round(
            df["volume"].corr(df["volatility"]),
            3
        )
    )

with c2:
    st.metric(
        "ISV ↔ Volatility",
        round(
            df["isv"].corr(df["volatility"]),
            3
        )
    )

with c3:
    st.metric(
        "Sentiment ↔ Return",
        round(
            df["avg_sentiment"].corr(df["daily_return"]),
            3
        )
    )
st.header("📌 Relationship Insights")

st.markdown("""
### Main Findings

✅ Discussion Volume showed the strongest relationship with volatility.

❌ Investor Sentiment Variance (ISV) was not statistically significant.

❌ Average Sentiment did not significantly predict returns.

⚠️ Social-media attention appears more informative than sentiment polarity.

### Interpretation

The results suggest that investor attention, measured through discussion volume,
has greater explanatory power for market volatility than sentiment-based measures.
""")