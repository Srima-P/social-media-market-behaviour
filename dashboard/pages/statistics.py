import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
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
BASE_DIR = Path(__file__).resolve().parent

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
# STATISTICAL RESULTS
# ==================================================

st.header("📊 Statistical Results")
st.subheader("Correlation Analysis")

corr_vol = round(df["volume"].corr(df["volatility"]), 3)
corr_isv = round(df["isv"].corr(df["volatility"]), 3)
corr_sent = round(df["avg_sentiment"].corr(df["daily_return"]), 3)

corr_df = pd.DataFrame({
    "Relationship": [
        "Volume ↔ Volatility",
        "ISV ↔ Volatility",
        "Sentiment ↔ Return"
    ],
    "Correlation": [
        corr_vol,
        corr_isv,
        corr_sent
    ]
})

st.dataframe(corr_df, width="stretch")
st.subheader("Regression Findings")

regression_results = pd.DataFrame({
    "Variable": [
        "ISV",
        "Discussion Volume",
        "Sentiment Velocity",
        "Comments"
    ],
    "Finding": [
        "Not Significant",
        "Significant Positive Predictor",
        "Not Significant",
        "Not Significant"
    ]
})

st.dataframe(regression_results, width="stretch")
st.subheader("Multicollinearity Check (VIF)")

vif_df = pd.DataFrame({
    "Metric": ["Maximum VIF"],
    "Value": ["< 2"]
})

st.dataframe(vif_df, width="stretch")

st.success("""
No multicollinearity problems detected.
All VIF values were between approximately 1 and 2.
""")
st.subheader("Granger Causality Results")

granger_df = pd.DataFrame({
    "Relationship": [
        "ISV → Volatility",
        "Sentiment → Return",
        "Volume → Volatility (GME)",
        "Volume → Volatility (AMC)",
        "Volume → Volatility (TSLA)"
    ],
    "Result": [
        "Not Significant",
        "Not Significant",
        "Significant",
        "Not Significant",
        "Not Significant"
    ]
})

st.dataframe(granger_df, width="stretch")
st.subheader("VAR Analysis")

var_df = pd.DataFrame({
    "Finding": [
        "Volume → Future Volatility",
        "Volatility → Future Volume"
    ],
    "Lag": [
        "Lag 3",
        "Lag 1"
    ],
    "p-value": [
        "0.030",
        "0.003"
    ]
})

st.dataframe(var_df, width="stretch")
st.subheader("Volume–Volatility Feedback Loop")

st.info("""
More Discussion Volume
        ↓
Higher Volatility
        ↓
More Investor Attention
        ↓
More Discussion Volume

Observed primarily for GME.
""")
st.subheader("Hypothesis Testing Results")

hypothesis_df = pd.DataFrame({
    "Hypothesis": [
        "ISV increases volatility",
        "Sentiment predicts returns",
        "Volume relates to volatility",
        "Volume predicts future volatility"
    ],
    "Result": [
        "❌ Rejected",
        "❌ Rejected",
        "✅ Supported",
        "⚠️ Partially Supported"
    ]
})

st.dataframe(hypothesis_df, width="stretch")
st.success("""
KEY RESEARCH FINDING

Discussion Volume emerged as the strongest and most consistent
social-media indicator of market volatility.

Investor Sentiment Variance (ISV), despite being the project's
novel contribution, did not demonstrate a statistically significant
relationship with volatility.
""")
st.subheader("Research Contribution")

st.markdown("""
### Contribution

This study introduced Investor Sentiment Variance (ISV)
as a quantitative measure of investor disagreement.

Although ISV was not found to be statistically significant,
the analysis revealed that discussion volume provides
stronger explanatory power for market volatility.

This finding suggests that investor attention may be
more important than investor sentiment when explaining
short-term market dynamics.
""")