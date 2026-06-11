# 🚕 NYC Taxi Demand Forecasting

## Project Overview

This project forecasts hourly taxi demand for NYC Taxi Zone 79 using a trained XGBoost machine learning model. The application follows a full-stack architecture by integrating a Streamlit frontend with a FastAPI backend.

The frontend provides an interactive dashboard where users can select a forecast horizon and visualize future taxi demand trends. The backend exposes REST API endpoints responsible for generating predictions using recursive forecasting techniques.

---

## Objectives

* Forecast hourly taxi demand for NYC Taxi Zone 79.
* Build an interactive dashboard for end users.
* Develop a FastAPI backend to serve predictions.
* Integrate frontend and backend components.
* Implement backend testing to ensure API reliability.

---

## Technology Stack

### Frontend

* Streamlit
* Plotly

### Backend

* FastAPI
* Uvicorn
* Pydantic

### Machine Learning

* XGBoost
* Scikit-learn
* Joblib

### Data Processing

* Pandas
* NumPy
* PyArrow

### Testing

* Pytest
* FastAPI TestClient

---

## Project Architecture

```
User
   ↓
Streamlit Frontend
   ↓
FastAPI Backend
   ↓
Forecasting Service
   ↓
XGBoost Model
   ↓
Forecast Predictions
```

---

## Folder Structure

```
YT_taxi_Frontend/

├── app.py                         # Streamlit application entry point
├── main.py                        # FastAPI application entry point
│
├── pages/
│   ├── demand_forecasting.py      # Frontend demand forecasting dashboard
│   └── __init__.py
│
├── services/
│   ├── forecasting_service.py     # Forecast generation logic
│   └── __init__.py
│
├── schemas/
│   ├── forecast_schema.py         # API request validation schema
│   └── __init__.py
│
├── tests/
│   └── test_forecasting.py        # Backend API tests
│
├── models/
│   └── final_xgboost_model.pkl    # Trained XGBoost model
│
├── config/
│   └── feature_order.json         # Feature order used during training
│
├── data/
│   └── hourly_demand.parquet      # Historical hourly demand data
│
├── requirements.txt               # Project dependencies
│
└── README.md
```

---

## Frontend Features Implemented

### 1. Interactive Dashboard

Developed using Streamlit to provide a simple and user-friendly interface.

Features include:

* Forecast horizon selection
* Forecast generation button
* Forecast results display
* Summary metrics visualization
* Interactive demand trend visualization
* Forecast result download functionality

---

### 2. Forecast Configuration

Users can select forecast horizons directly from the dashboard:

* 24 Hours
* 48 Hours
* 72 Hours

---

### 3. Forecast Results Table

The dashboard displays generated forecasts in a tabular format containing:

* Forecast Timestamp
* Forecasted Taxi Demand

---

### 4. Forecast Summary Metrics

The following metrics are automatically computed and displayed:

* Average Forecasted Demand
* Maximum Forecasted Demand
* Minimum Forecasted Demand

---

### 5. Interactive Visualization

Implemented using Plotly.

Features:

* Interactive line charts
* Zoom and pan functionality
* Hover tooltips displaying exact demand values
* Responsive layout support

---

### 6. CSV Export Functionality

Users can download generated forecast results as CSV files for further analysis.

---

## Backend Features Implemented

### FastAPI REST API

Implemented API endpoints to serve demand forecasts.

### Available Endpoints

#### Home Endpoint

```
GET /
```

Returns API status information.

---

#### Forecast Endpoint

```
POST /forecast
```

Accepts forecast requests and returns future taxi demand predictions.

Example Request:

```json
{
    "forecast_horizon": 24
}
```

---

## Forecasting Methodology

The system uses recursive forecasting with a trained XGBoost model.

Features utilized include:

### Temporal Features

* Hour of Day
* Day of Week
* Month
* Week Number
* Weekend Indicator

### Lag Features

* Lag 1 Hour
* Lag 24 Hours
* Lag 168 Hours

### Rolling Features

* 24-Hour Rolling Mean
* 168-Hour Rolling Mean

Predictions generated at each step are recursively used to generate future forecasts.

---

## API Documentation

FastAPI automatically generates Swagger documentation.

Run:

```bash
uvicorn main:app --reload
```


Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Backend Testing

Backend APIs were tested using Pytest and FastAPI TestClient.

### Tested Scenarios

* API accessibility validation
* Successful response validation
* Forecast generation validation
* Output length verification

Run tests:

```bash
pytest
```

Result:

```
1 passed
```

---

## Installation Guide

### Clone Repository

```bash
git clone <repository_url>

cd YT_taxi_Frontend
```

---

### Create Environment

```bash
conda create -n myenv python=3.12

conda activate myenv
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Backend

```bash
uvicorn main:app --reload
```

Backend URL:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Running the Frontend

```bash
streamlit run app.py
```

Frontend URL:

```
http://localhost:8501
```

---

## Current Project Status

### Use Case 1: Taxi Demand Forecasting

Completed:

* XGBoost forecasting model integration
* FastAPI backend implementation
* Streamlit frontend implementation
* Frontend-backend integration
* Interactive Plotly visualizations
* CSV export functionality
* Swagger API documentation
* Backend unit testing using Pytest

---

## Future Enhancements

* Support forecasting for multiple NYC zones.
* Add additional forecasting use cases.
* Containerization using Docker.
* Cloud deployment.
* CI/CD integration.

---

## Author

Developed as part of the NYC Taxi Demand Forecasting project to demonstrate end-to-end machine learning application development using FastAPI and Streamlit.
