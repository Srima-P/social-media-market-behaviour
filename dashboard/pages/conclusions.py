import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
# ==================================================
# FINAL CONCLUSIONS
# ==================================================

st.header("🎯 Final Conclusions")
st.subheader("Executive Summary")

st.info("""
This project investigated whether social-media activity
can explain or predict stock market behavior.

Using Reddit discussions related to GME, AMC, and TSLA,
social-media sentiment features were extracted using FinBERT.

A novel metric, Investor Sentiment Variance (ISV),
was introduced to measure investor disagreement.

The resulting social-media features were statistically
compared against market returns and volatility.
""")
st.subheader("Research Workflow")

st.code("""
Social Media Data
        ↓
FinBERT Sentiment Analysis
        ↓
Sentiment Metrics
        ↓
Investor Sentiment Variance (ISV)
        ↓
Market Data Collection
        ↓
Statistical Analysis
        ↓
Research Findings
        ↓
Interactive Dashboard
""")
st.subheader("Main Findings")

st.success("""
✅ Discussion Volume showed the strongest relationship with volatility.

✅ Evidence of a Volume–Volatility feedback loop was found for GME.

❌ Investor Sentiment Variance (ISV) was not statistically significant.

❌ Average Sentiment did not significantly predict returns.
""")

st.subheader("Final Research Insight")

st.warning("""
Investor attention, measured through discussion volume,
appears to explain market volatility more effectively
than investor sentiment or investor disagreement.

The quantity of discussion mattered more than
the sentiment contained within the discussion.
""")

st.subheader("Research Contribution")

st.markdown("""
### Novel Contribution

This study proposed Investor Sentiment Variance (ISV)
as a quantitative measure of investor disagreement.

Although ISV was not found to be statistically significant,
the framework demonstrates how disagreement can be measured
and tested using social-media data.

The study further identified discussion volume as a stronger
social-media signal for understanding market volatility.
""")

st.subheader("Limitations")

st.markdown("""
- Only three stocks were analyzed.
- Data was limited to WallStreetBets discussions.
- Analysis covered a specific historical period.
- FinBERT sentiment may not capture all market nuances.
- External market events were not explicitly modeled.
""")

st.subheader("Future Scope")

st.markdown("""
### Research Extensions

- Real-time social-media monitoring
- Multi-platform analysis
- LSTM forecasting models
- Transformer-based prediction systems
- Event-driven sentiment analysis

### Industry Applications

- Risk monitoring
- Market surveillance
- Investor behavior analysis
- Trading support systems
""")

st.subheader("Final Hypothesis Evaluation")

final_results = pd.DataFrame({
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

st.dataframe(final_results, width="stretch")

st.subheader("One-Minute Project Summary")

st.success("""
This project developed a behavioral-finance framework
that converts social-media discussions into quantitative
indicators using NLP and sentiment analysis.

While Investor Sentiment Variance (ISV) did not show a
significant relationship with market volatility,
discussion volume consistently emerged as the strongest
social-media indicator of volatility.

The findings suggest that investor attention may be more
important than investor sentiment when explaining short-term
market dynamics.
""")