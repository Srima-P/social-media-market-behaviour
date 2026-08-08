# Quantifying the Collective Voice: Assessing the Impact of Social Media Sentiment Variance and Discussion Volume on Intraday Market Dynamics

## Overview

Financial markets are increasingly influenced by information shared on social media platforms. Retail investors actively discuss stocks, share opinions, and react to market events through online communities. This project investigates whether social-media activity can explain or predict stock market behavior.

The study focuses on three highly discussed stocks:

* GME (GameStop)
* AMC Entertainment
* TSLA (Tesla)

Using Natural Language Processing (NLP), sentiment analysis, feature engineering, and time-series statistical methods, the project evaluates how social-media discussions relate to stock returns and volatility.

---

## Research Objectives

This project aims to answer the following questions:

1. Does investor disagreement increase market volatility?
2. Can social-media sentiment predict stock returns?
3. Does discussion volume relate to market volatility?
4. Can social-media activity predict future market volatility?

---

## Methodology

### Phase 1 — Problem Definition

Defined the research problem and identified the relationship between social-media activity and stock market dynamics.

---

### Phase 2 — Data Collection

#### Data Source

WallStreetBets Reddit Dataset

#### Selected Stocks

| Stock |  Posts |
| ----- | -----: |
| GME   | 14,745 |
| AMC   |  5,161 |
| TSLA  |  1,078 |

**Total Posts Processed:** 20,984

---

### Phase 3 — Sentiment Analysis

#### Model Used

FinBERT

FinBERT is a transformer-based language model specifically designed for financial text sentiment analysis.

#### Extracted Features

* Positive Sentiment
* Neutral Sentiment
* Negative Sentiment

#### Daily Aggregations

* Average Sentiment
* Sentiment Velocity

---

### Phase 4 — Feature Engineering

#### Investor Sentiment Variance (ISV)

A novel metric introduced in this project to quantify investor disagreement.

Formula:

ISV = Σ(Si − S̄)² / N

Where:

* Si = Individual sentiment score
* S̄ = Average sentiment
* N = Number of posts

#### Interpretation

* High ISV → Strong disagreement among investors
* Low ISV → Investor consensus

#### Additional Features

* Discussion Volume
* Average Score
* Average Comments
* Sentiment Velocity

---

### Phase 5 — Market Data Processing

Market data was collected and synchronized with the sentiment dataset.

#### Market Features

* Daily Return
* Intraday Return
* Volatility
* Abnormal Volume

#### Final Dataset Sizes

| Dataset | Shape    |
| ------- | -------- |
| GME     | (73, 11) |
| AMC     | (72, 11) |
| TSLA    | (90, 11) |

---

### Phase 6 — Statistical Analysis

#### Techniques Used

* Correlation Analysis
* Multiple Linear Regression
* Variance Inflation Factor (VIF)
* Augmented Dickey-Fuller Test (ADF)
* Granger Causality
* Vector Autoregression (VAR)

---

## Key Findings

### Hypothesis 1

**Investor disagreement (ISV) increases volatility**

Result:

❌ Rejected

No statistically significant relationship was found between ISV and market volatility.

---

### Hypothesis 2

**Sentiment predicts returns**

Result:

❌ Rejected

Average sentiment was not a significant predictor of stock returns.

---

### Hypothesis 3

**Discussion volume relates to volatility**

Result:

✅ Supported

Discussion volume showed the strongest positive relationship with market volatility.

---

### Hypothesis 4

**Discussion volume predicts future volatility**

Result:

⚠️ Partially Supported

Evidence was primarily observed for GME through Granger causality and VAR analysis.

---

## Main Research Insight

The most important finding of the study is:

> Discussion volume emerged as the strongest and most consistent social-media indicator of market volatility.

While Investor Sentiment Variance (ISV) was introduced as a novel measure of investor disagreement, empirical testing showed that investor attention, measured through discussion volume, had greater explanatory power than sentiment-based measures.

---

## Interactive Dashboard

A Streamlit dashboard was developed to visualize:

### Social Media Analytics

* Discussion Volume
* Average Sentiment
* Investor Sentiment Variance (ISV)
* Sentiment Velocity

### Market Analytics

* Daily Returns
* Intraday Returns
* Volatility
* Abnormal Trading Volume

### Relationship Analysis

* ISV vs Volatility
* Volume vs Volatility
* Sentiment vs Returns
* Correlation Heatmaps

### Statistical Results

* Regression Findings
* VIF Analysis
* Granger Causality Results
* VAR Results
* Hypothesis Evaluation

---

## Technology Stack

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Visualization

* Plotly
* Matplotlib
* Streamlit

### Machine Learning & NLP

* FinBERT
* Transformers
* PyTorch

### Statistical Analysis

* Statsmodels
* Scikit-learn

### Financial Data

* Yahoo Finance (yfinance)

---

## Project Structure

```text
project/
│
├── notebooks/
│   ├── phase2_data_collection.ipynb
│   ├── phase3_sentiment_analysis.ipynb
│   ├── phase4_feature_engineering.ipynb
│   ├── phase5_market_processing.ipynb
│   └── phase6_statistical_analysis.ipynb
│
├── datasets/
│   ├── final_gme_dataset.csv
│   ├── final_amc_dataset.csv
│   └── final_tsla_dataset.csv
│
├── dashboard/
│   ├── app.py
│   └── requirements.txt
│
├── images/
│
├── README.md
│
└── .gitignore
```

---

## Future Scope

Potential extensions of this work include:

* Real-time social-media monitoring
* Multi-platform sentiment analysis
* Transformer-based forecasting models
* Event-driven market prediction systems
* Deep learning approaches for volatility forecasting

---

## Conclusion

This project presents a complete end-to-end behavioral finance framework that combines social-media analytics, NLP, feature engineering, and time-series statistical analysis.

The findings suggest that investor attention may be more important than investor sentiment when explaining short-term market volatility, highlighting the growing influence of collective online discussion in modern financial markets.
