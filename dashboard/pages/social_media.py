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
# --------------------------------------------------

gme = load_data("C:\Users\srima\social media market analysis\dashboard\final_gme_dataset.csv")
amc = load_data("C:\Users\srima\social media market analysis\dashboard\final_amc_dataset.csv")
tsla = load_data("C:\Users\srima\social media market analysis\dashboard\final_tsla_dataset.csv")


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
# SOCIAL MEDIA ANALYTICS
# ==================================================


st.header("📱 Social Media Analytics")


# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------


k1, k2, k3, k4 = st.columns(4)


with k1:
    st.metric(
        "Total Posts",
        int(df["volume"].sum())
    )


with k2:
    st.metric(
        "Average Sentiment",
        round(df["avg_sentiment"].mean(), 3)
    )


with k3:
    st.metric(
        "Average ISV",
        round(df["isv"].mean(), 3)
    )


with k4:
    st.metric(
        "Maximum Volume",
        int(df["volume"].max())
    )


# --------------------------------------------------
# DISCUSSION VOLUME TREND
# --------------------------------------------------


st.subheader("Discussion Volume Trend")


fig_volume = px.line(
    df,
    x="date",
    y="volume",
    title=f"{stock} Discussion Volume Over Time",
    markers=True
)


fig_volume.update_layout(
    xaxis_title="Date",
    yaxis_title="Discussion Volume"
)


st.plotly_chart(
    fig_volume,
    use_container_width=True
)


# --------------------------------------------------
# SENTIMENT TREND
# --------------------------------------------------


st.subheader("Average Sentiment Trend")


fig_sentiment = px.line(
    df,
    x="date",
    y="avg_sentiment",
    title=f"{stock} Average Sentiment Over Time",
    markers=True
)


fig_sentiment.update_layout(
    xaxis_title="Date",
    yaxis_title="Average Sentiment"
)


st.plotly_chart(
    fig_sentiment,
    use_container_width=True
)


# --------------------------------------------------
# ISV TREND
# --------------------------------------------------


st.subheader("Investor Sentiment Variance (ISV)")


fig_isv = px.line(
    df,
    x="date",
    y="isv",
    title=f"{stock} Investor Sentiment Variance",
    markers=True
)


fig_isv.update_layout(
    xaxis_title="Date",
    yaxis_title="ISV"
)


st.plotly_chart(
    fig_isv,
    use_container_width=True
)


# --------------------------------------------------
# SENTIMENT VELOCITY TREND
# --------------------------------------------------


st.subheader("Sentiment Velocity Trend")


fig_velocity = px.line(
    df,
    x="date",
    y="sentiment_velocity",
    title=f"{stock} Sentiment Velocity",
    markers=True
)


fig_velocity.update_layout(
    xaxis_title="Date",
    yaxis_title="Sentiment Velocity"
)


st.plotly_chart(
    fig_velocity,
    use_container_width=True
)


# --------------------------------------------------
# DISTRIBUTION CHARTS
# --------------------------------------------------


st.header("📈 Distribution Analysis")


d1, d2 = st.columns(2)


with d1:


    fig_vol_dist = px.histogram(
        df,
        x="volume",
        nbins=20,
        title="Discussion Volume Distribution"
    )


    st.plotly_chart(
        fig_vol_dist,
        use_container_width=True
    )


with d2:


    fig_isv_dist = px.histogram(
        df,
        x="isv",
        nbins=20,
        title="ISV Distribution"
    )


    st.plotly_chart(
        fig_isv_dist,
        use_container_width=True
    )


# --------------------------------------------------
# INSIGHTS
# --------------------------------------------------


st.header("🔍 Social Media Insights")


st.info("""
Discussion Volume measures investor attention.


Average Sentiment measures overall market mood.


Investor Sentiment Variance (ISV) measures disagreement among investors.


Sentiment Velocity measures how rapidly sentiment changes over time.


These social-media variables were later evaluated against market returns and volatility during Phase 6 statistical testing.
""")


# --------------------------------------------------
# PROJECT FINDINGS
# --------------------------------------------------


st.header("📑 Current Research Findings")


st.success("""
✅ Discussion Volume showed the strongest relationship with volatility.


❌ Investor Sentiment Variance (ISV) was not statistically significant.


❌ Average Sentiment did not significantly predict returns.


⚠️ Evidence of a Volume–Volatility feedback loop was found primarily for GME.
""")


# --------------------------------------------------
# FOOTER
# --------------------------------------------------


st.markdown("---")