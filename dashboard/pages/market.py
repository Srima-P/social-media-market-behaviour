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
# MARKET ANALYTICS
# ==================================================


st.header("📈 Market Analytics")


# --------------------------------------------------
# MARKET KPI CARDS
# --------------------------------------------------


m1, m2, m3, m4 = st.columns(4)


with m1:
    st.metric(
        "Avg Daily Return",
        f"{df['daily_return'].mean():.4f}"
    )


with m2:
    st.metric(
        "Avg Volatility",
        f"{df['volatility'].mean():.4f}"
    )


with m3:
    st.metric(
        "Max Volatility",
        f"{df['volatility'].max():.4f}"
    )


with m4:
    st.metric(
        "Avg Abnormal Volume",
        f"{df['abnormal_volume'].mean():.2f}"
    )


# --------------------------------------------------
# DAILY RETURN TREND
# --------------------------------------------------


st.subheader("Daily Return Trend")


fig_daily_return = px.line(
    df,
    x="date",
    y="daily_return",
    title=f"{stock} Daily Returns",
    markers=True
)


fig_daily_return.update_layout(
    xaxis_title="Date",
    yaxis_title="Daily Return"
)


st.plotly_chart(
    fig_daily_return,
    use_container_width=True
)


# --------------------------------------------------
# INTRADAY RETURN TREND
# --------------------------------------------------


st.subheader("Intraday Return Trend")


fig_intraday = px.line(
    df,
    x="date",
    y="intraday_return",
    title=f"{stock} Intraday Returns",
    markers=True
)


fig_intraday.update_layout(
    xaxis_title="Date",
    yaxis_title="Intraday Return"
)


st.plotly_chart(
    fig_intraday,
    use_container_width=True
)


# --------------------------------------------------
# VOLATILITY TREND
# --------------------------------------------------


st.subheader("Volatility Trend")


fig_volatility = px.line(
    df,
    x="date",
    y="volatility",
    title=f"{stock} Volatility Over Time",
    markers=True
)


fig_volatility.update_layout(
    xaxis_title="Date",
    yaxis_title="Volatility"
)


st.plotly_chart(
    fig_volatility,
    use_container_width=True
)


# --------------------------------------------------
# ABNORMAL VOLUME TREND
# --------------------------------------------------


st.subheader("Abnormal Trading Volume")


fig_abnormal = px.line(
    df,
    x="date",
    y="abnormal_volume",
    title=f"{stock} Abnormal Trading Volume",
    markers=True
)


fig_abnormal.update_layout(
    xaxis_title="Date",
    yaxis_title="Abnormal Volume"
)


st.plotly_chart(
    fig_abnormal,
    use_container_width=True
)


# --------------------------------------------------
# DISTRIBUTIONS
# --------------------------------------------------


st.header("📊 Market Distributions")


dist1, dist2 = st.columns(2)


with dist1:


    fig_vol_dist = px.histogram(
        df,
        x="volatility",
        nbins=20,
        title="Volatility Distribution"
    )


    st.plotly_chart(
        fig_vol_dist,
        use_container_width=True
    )


with dist2:


    fig_return_dist = px.histogram(
        df,
        x="daily_return",
        nbins=20,
        title="Daily Return Distribution"
    )


    st.plotly_chart(
        fig_return_dist,
        use_container_width=True
    )


# --------------------------------------------------
# MARKET INSIGHTS
# --------------------------------------------------


st.header("🔍 Market Insights")


st.info("""
Daily Return measures overall stock performance.


Intraday Return measures price movement within a trading day.


Volatility measures price fluctuations and market uncertainty.


Abnormal Volume measures trading activity relative to its recent average.


These variables were used as market indicators in the statistical analysis phase.
""")