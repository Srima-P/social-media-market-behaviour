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
# --------------------------------------------------
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

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📈 Social Media & Market Dynamics Dashboard")

st.markdown("""
### Project Title

**Quantifying the Collective Voice: Assessing the Impact of Social Media Sentiment Variance and Discussion Volume on Intraday Market Dynamics**
""")

# --------------------------------------------------
# DATASET SUMMARY
# --------------------------------------------------

st.header("📊 Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows", len(df))

with col2:
    st.metric("Columns", len(df.columns))

with col3:
    st.metric(
        "Date Range",
        f"{df['date'].min().date()} → {df['date'].max().date()}"
    )

# --------------------------------------------------
# SHAPES
# --------------------------------------------------

st.subheader("Dataset Shapes")

s1, s2, s3 = st.columns(3)

with s1:
    st.info(f"GME: {gme.shape}")

with s2:
    st.info(f"AMC: {amc.shape}")

with s3:
    st.info(f"TSLA: {tsla.shape}")

# --------------------------------------------------
# AVAILABLE VARIABLES
# --------------------------------------------------

st.subheader("Variables")

st.write(df.columns.tolist())

# --------------------------------------------------
# SAMPLE DATA
# --------------------------------------------------

st.subheader(f"{stock} Sample Data")

st.dataframe(df.head(10), use_container_width=True)

