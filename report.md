🚖 NYC Taxi Demand Forecasting & Real-Time Decision Support System

📄 Project Report

1. 📌 Abstract

Urban taxi systems generate large volumes of spatio-temporal data that can be leveraged to improve demand prediction, optimize driver allocation, and enhance operational efficiency. This project presents an end-to-end machine learning-based system for NYC taxi demand forecasting, trip analysis, anomaly detection, hotspot identification, and real-time decision support.

The system integrates machine learning models with a FastAPI backend and a Streamlit-based interactive dashboard to provide real-time analytics and actionable insights.

2. 🎯 Problem Statement

Taxi services in metropolitan cities like New York face challenges such as:

Unpredictable demand fluctuations across regions
Inefficient driver distribution
Delayed response to demand spikes
Lack of real-time decision support tools

The objective of this project is to build a system that:

Predicts taxi demand
Identifies high-demand hotspots
Detects anomalies in trip patterns
Optimizes driver positioning
Provides real-time analytics for decision-making


3. 🧠 Objectives
To forecast taxi demand using historical data
To predict trip duration based on trip attributes
To identify spatial hotspots of demand
To detect anomalies in taxi activity
To recommend optimal driver positioning
To build a real-time analytics dashboard


4. 🏗️ System Architecture

The system follows a layered architecture:

Frontend Layer: Streamlit Dashboard
Backend Layer: FastAPI REST API
Service Layer: Business logic for ML inference
Model Layer: Trained machine learning models
Data Layer: NYC taxi trip dataset with engineered features
Flow:

Streamlit UI → FastAPI → ML Services → Models → Predictions → Dashboard

5. ⚙️ Technology Stack
Python
FastAPI (Backend API)
Streamlit (Frontend Dashboard)
Pandas, NumPy (Data Processing)
Scikit-learn / XGBoost (ML Models)
Plotly (Visualization)
Joblib (Model Serialization)


6. 📊 Modules Implemented
6.1 Taxi Demand Forecasting

Predicts future taxi demand based on historical patterns and temporal features.

Model: Time-series regression / ML regression model
Output: Forecasted demand for next time intervals
6.2 Trip Duration Prediction

Estimates trip duration using features like pickup/drop location, distance, and time.

Model: Regression-based ML model
Output: Estimated trip time
6.3 Hotspot Detection

Identifies high-demand zones using clustering and aggregation techniques.

Model: Clustering / statistical aggregation
Output: Top demand zones
6.4 Anomaly Detection

Detects unusual patterns in taxi demand or trip behavior.

Model: Isolation Forest / anomaly detection model
Output: Alerts for unusual activity
6.5 Driver Positioning System

Recommends optimal zones for drivers based on predicted demand.

Logic: Rule-based + ML-based decision system
Output: Recommended high-demand zone
6.6 Real-Time Analytics Dashboard (Final Use Case)

A real-time interactive dashboard that integrates all modules.

Features:

Live demand visualization
Forecast trends
Hotspot heatmaps
Anomaly alerts
Driver recommendation system


7. 🔄 System Workflow
Raw taxi data is processed and feature-engineered
ML models are trained and saved
FastAPI loads models and exposes endpoints
Streamlit dashboard consumes APIs
Real-time analytics are displayed
Decision support is generated dynamically


8. 📡 API Endpoints
/forecast → Demand forecasting
/predict-duration → Trip duration prediction
/hotspots → Hotspot detection
/anomaly/predict → Anomaly detection
/recommend-driver-position → Driver optimization
/live-demand → Real-time demand snapshot


9. 📈 Results

The system successfully:

Predicts taxi demand trends
Identifies high-demand regions in real time
Detects anomalies in taxi activity
Provides actionable driver recommendations
Visualizes system behavior through an interactive dashboard


10. 🖥️ User Interface

The Streamlit dashboard includes:

KPI metrics (Demand, Max demand, Avg demand)
Zone-wise demand bar chart
Forecast line chart
Heatmap of taxi hotspots
Live anomaly alerts
Decision recommendation panel


11. 🚀 Key Features
End-to-end ML pipeline
Real-time API-based architecture
Interactive dashboard
Modular service-based backend
Decision support system


12. 📌 Conclusion

This project demonstrates a complete machine learning-driven decision support system for urban taxi demand management. By integrating predictive analytics with real-time visualization, the system helps optimize driver allocation and improve operational efficiency.

The combination of FastAPI and Streamlit provides a scalable and interactive architecture suitable for real-world deployment scenarios.

13. 🔮 Future Scope
Integration with live GPS taxi data
Kafka-based streaming pipeline for true real-time updates
Deployment on cloud (AWS/GCP)
Mobile application for drivers
Advanced deep learning models for demand forecasting