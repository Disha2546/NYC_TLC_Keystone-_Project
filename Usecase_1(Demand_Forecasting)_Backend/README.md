# NYC Taxi Demand Forecasting using XGBoost and Streamlit

## 1. Project Overview

This project aims to forecast hourly taxi demand for New York City taxi zones using historical trip data. Accurate demand forecasting helps taxi operators optimize resource allocation, reduce passenger waiting times, improve fleet management, and support operational decision-making.

The project follows a complete machine learning lifecycle including:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Feature engineering
* Model development
* Model evaluation
* Recursive multi-step forecasting
* Streamlit application deployment

---

# 2. Problem Statement

Predict future hourly taxi demand for NYC taxi zones using historical trip records.

### Objective

Develop a machine learning model capable of forecasting taxi demand for the next:

* 24 hours
* 48 hours
* 72 hours

using historical demand patterns and time-based features.

---

# 3. Business Understanding

Accurate taxi demand forecasting provides several benefits:

* Improved fleet utilization
* Better driver allocation
* Reduced passenger waiting times
* Increased operational efficiency
* Data-driven decision making

This project demonstrates how machine learning can support transportation demand planning.

---

# 4. Dataset Description

## Data Source

NYC Yellow Taxi Trip Records.

## Initial Dataset Characteristics

The raw dataset contained trip-level information such as:

* Pickup datetime
* Dropoff datetime
* Pickup location ID (PULocationID)
* Dropoff location ID
* Passenger count
* Trip distance
* Fare amount

---

# 5. Data Preprocessing

The following preprocessing steps were performed:

## Timestamp Conversion

Pickup timestamps were converted into datetime format for temporal analysis.

## Hourly Aggregation

Trip records were aggregated into hourly demand counts.

Resulting dataset structure:

| hour             | PULocationID | demand |
| ---------------- | ------------ | ------ |
| 2026-01-01 00:00 | 79           | 432    |
| 2026-01-01 01:00 | 79           | 459    |

Demand represents the number of trips occurring during each hour.

---

# 6. Zone Selection Strategy

Instead of forecasting all zones simultaneously, a single-zone forecasting approach was adopted.

## Zone Selection Process

The zone with the highest number of observations was selected:

Selected Zone: 79

Total Observations: 745

## Reason for Single Zone Selection

* Highest data availability.
* Reduced sparsity issues.
* Simplified modeling process.
* Allowed development of a robust baseline forecasting system.
* Reduced computational complexity.

This approach is appropriate for an initial forecasting prototype.

---

# 7. Exploratory Data Analysis (EDA)

EDA was conducted to understand demand behavior.

Key analyses included:

## Demand Distribution Analysis

* Examined variability in hourly demand.
* Identified skewness and outliers.

## Time-Based Demand Patterns

Analyzed demand variations across:

* Hours of the day
* Days of the week
* Weekends versus weekdays

## Seasonal Behavior

Observed recurring temporal demand patterns indicating seasonality.

Findings suggested that demand is strongly influenced by temporal factors.

---

# 8. Feature Engineering

Feature engineering transformed raw timestamps into predictive variables.

## Calendar Features

### hour_of_day

Represents the hour of occurrence.

Purpose:

Captures daily demand cycles.

---

### day_of_week

Represents weekday index:

0 = Monday

6 = Sunday

Purpose:

Captures weekly seasonality.

---

### day_name

Numerical representation of weekdays.

Purpose:

Provides additional categorical temporal information.

---

### month

Represents calendar month.

Purpose:

Captures monthly trends.

---

### week

Represents ISO week number.

Purpose:

Captures weekly demand changes.

---

### is_weekend

Binary indicator:

0 = Weekday

1 = Weekend

Purpose:

Differentiates weekend demand behavior.

---

# 9. Lag Feature Engineering

Lag features capture previous demand information.

## lag_1

Demand observed one hour earlier.

Purpose:

Captures immediate temporal dependency.

---

## lag_24

Demand observed 24 hours earlier.

Purpose:

Captures daily repeating patterns.

---

## lag_168

Demand observed 168 hours earlier.

Equivalent to:

7 days × 24 hours

Purpose:

Captures weekly seasonality.

Reason for inclusion:

Taxi demand often follows weekly behavioral patterns.

---

# 10. Rolling Features

Rolling statistics summarize recent demand history.

## rolling_mean_24

Average demand over previous 24 hours.

Purpose:

Smooths short-term fluctuations.

---

## rolling_mean_168

Average demand over previous 168 hours.

Purpose:

Captures long-term weekly trends.

---

# 11. Data Splitting Strategy

Chronological splitting was used to avoid data leakage.

Training Data:

First 24 days.

Validation Data:

Next 3 days.

Testing Data:

Final 4 days.

Reason:

Time series forecasting requires preserving temporal order.

Random splitting was avoided because future observations must never influence past predictions.

---

# 12. Model Selection

## Selected Model

XGBoost Regressor.

---

# 13. Why XGBoost?

XGBoost was selected because:

* Handles nonlinear relationships effectively.
* Performs well on tabular data.
* Works efficiently with engineered lag features.
* Requires relatively smaller datasets.
* Provides strong predictive performance.
* Faster training compared to many alternatives.

---

# 14. Model Training

The XGBoost model was trained using engineered features.

Input Features:

* PULocationID
* hour_of_day
* day_of_week
* day_name
* month
* week
* is_weekend
* lag_1
* lag_24
* lag_168
* rolling_mean_24
* rolling_mean_168

Target Variable:

demand

---

# 15. Forecasting Approach

Recursive forecasting was implemented.

Process:

1. Predict next hour demand.
2. Add prediction to historical sequence.
3. Generate updated lag features.
4. Predict subsequent hour.
5. Repeat until desired forecast horizon is achieved.

Forecast horizons:

* 24 hours
* 48 hours
* 72 hours

---

# 16. Why Recursive Forecasting?

Future lag values are unknown during deployment.

Recursive forecasting allows:

* Multi-step prediction.
* Automatic generation of future lag variables.
* Real-world deployment capability.

Limitation:

Forecast errors may accumulate over longer horizons.

---

# 17. Model Evaluation Metrics

## Mean Absolute Error (MAE)

Measures average magnitude of prediction errors.

Lower values indicate better performance.

---

## Root Mean Squared Error (RMSE)

Penalizes larger forecasting errors more heavily.

Lower values indicate better predictive accuracy.

---

# 18. Validation Results

Validation forecasting was performed using recursive prediction.

Forecasts were compared against actual observations.

Residual analysis was conducted to assess model behavior.

Observed errors were attributed to:

* Limited training duration.
* Complex taxi demand patterns.
* Error accumulation in recursive forecasting.

---

# 19. Model Saving

Trained artifacts were persisted for deployment.

Saved files:

## final_xgboost_model.pkl

Stores trained XGBoost model.

Purpose:

Used during deployment.

---

## feature_order.json

Stores exact feature ordering.

Purpose:

Prevents feature mismatch errors during prediction.

---

# 20. Streamlit Deployment

An interactive Streamlit application was developed.

Features:

* Forecast horizon selection:

  * 24 hours
  * 48 hours
  * 72 hours

* Automatic feature generation.

* Recursive forecasting.

* Forecast table visualization.

* Forecast summary metrics.

* Forecast trend graph.

* CSV export functionality.

---

# 21. Deployment Workflow

Historical Data

↓

Feature Generation

↓

Recursive Forecasting

↓

Demand Prediction

↓

Visualization

↓

CSV Download

---

# 22. Project Limitations

Several limitations exist:

* Only one taxi zone was modeled.
* Limited historical period available.
* External factors were excluded:

  * Weather
  * Holidays
  * Events
* Recursive forecasting accumulates errors over time.

---

# 23. Future Improvements

Potential enhancements include:

* Forecasting all NYC zones simultaneously.
* Incorporating weather data.
* Including holiday indicators.
* Exploring LightGBM and CatBoost.
* Implementing LSTM networks.
* Using Temporal Fusion Transformers.
* Hyperparameter optimization using Optuna.

---

# 24. Key Learnings

This project provided practical experience in:

* Time series forecasting.
* Feature engineering.
* Recursive forecasting.
* Machine learning model development.
* Model evaluation.
* Streamlit deployment.
* End-to-end ML project implementation.

---

# 25. Conclusion

This project successfully developed and deployed a machine learning system capable of forecasting hourly NYC taxi demand using XGBoost.

The solution demonstrated the effectiveness of combining temporal feature engineering with gradient boosting techniques for time series forecasting.

The deployed Streamlit application provides an interactive interface for generating future demand forecasts, making the project both technically complete and practically useful.

This project represents a complete end-to-end machine learning workflow, covering data preparation through production deployment.
