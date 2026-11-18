#  Earthquake Activity Analysis and Forecasting Using Time Series Models

### Real-Time Global Earthquake Activity Analysis and Five-Day Forecasting

---

##  1. Project Overview

Earthquakes are natural disasters that can cause significant damage to human life, infrastructure and the environment. Analyzing historical earthquake patterns can help researchers understand seismic activity and study changes in earthquake frequency over time.

This project focuses on analyzing global earthquake activity using historical earthquake records obtained from the **USGS Earthquake Catalog**.

Time series forecasting techniques are implemented to analyze daily earthquake frequency and forecast earthquake activity for the next five days.

Five forecasting models are developed and compared:

1. ARIMA
2. SARIMA
3. Recurrent Neural Network (RNN)
4. Long Short-Term Memory (LSTM)
5. Facebook Prophet

An interactive Streamlit dashboard is developed to visualize earthquake activity, compare model performance and display future forecasts.

##  2. Problem Statement

Earthquake datasets contain valuable information about the frequency, magnitude, depth and geographical distribution of seismic events.

However, analyzing large volumes of historical earthquake data manually is difficult.

The objective of this project is to develop a time series forecasting system that analyzes historical global earthquake activity, identifies temporal patterns and forecasts daily earthquake counts using multiple statistical and deep learning models.

##  3. Project Objectives

- Collect historical earthquake records from the USGS Earthquake Catalog.
- Analyze global earthquake activity over time.
- Perform Exploratory Data Analysis (EDA).
- Study trends, seasonality and stationarity in earthquake data.
- Apply time series forecasting techniques.
- Implement ARIMA and SARIMA statistical models.
- Implement RNN and LSTM deep learning models.
- Apply Facebook Prophet for forecasting.
- Evaluate model performance using MAE, MSE and RMSE.
- Compare the forecasting performance of all five models.
- Develop an interactive Streamlit dashboard.
- Forecast daily earthquake counts for the next five days.

## 4. Dataset Description

**Dataset Source:** USGS Earthquake Catalog

Official source: https://earthquake.usgs.gov/earthquakes/search/

The project uses global earthquake records covering approximately five years.

### Dataset Information

| Attribute | Description |
|---|---|
| Data Source | USGS Earthquake Catalog |
| Geographic Coverage | Global |
| Data Type | Time Series |
| Frequency | Daily |
| Historical Period | Approximately 2021–2026 |
| Main Target Variable | Daily Earthquake Count |
| Forecast Horizon | Next 5 Days |

### Important Dataset Features

| Feature | Description |
|---|---|
| Time | Date and time of earthquake |
| Latitude | Geographical latitude |
| Longitude | Geographical longitude |
| Magnitude | Earthquake magnitude |
| Depth | Earthquake depth |
| Place | Earthquake location |
| Earthquake Count | Number of earthquakes recorded per day |
| Average Magnitude | Average daily earthquake magnitude |
| Maximum Magnitude | Maximum daily earthquake magnitude |
| Average Depth | Average daily earthquake depth |

##  5. Exploratory Data Analysis (EDA)

Exploratory Data Analysis is performed to understand earthquake activity and identify important patterns.

The analysis includes:

- Dataset structure and dimensions.
- Missing value analysis.
- Duplicate record analysis.
- Statistical summary.
- Earthquake magnitude distribution.
- Daily earthquake frequency.
- Time series trend analysis.
- Autocorrelation analysis.
- Partial autocorrelation analysis.
- Time series decomposition.
- Stationarity testing using the Augmented Dickey-Fuller (ADF) test.
- First-order differencing.

##  6. Time Series Forecasting Models

Five different forecasting approaches are implemented and evaluated.

### 1. ARIMA (AutoRegressive Integrated Moving Average)

ARIMA is a statistical time series forecasting model that combines autoregression, differencing and moving averages.

It is used to identify temporal dependencies and forecast future earthquake counts.

### 2. SARIMA (Seasonal AutoRegressive Integrated Moving Average)

SARIMA extends ARIMA by incorporating seasonal components.

It is applied to investigate recurring patterns in daily earthquake activity.

### 3. RNN (Recurrent Neural Network)

RNN is a deep learning architecture designed to process sequential data.

It uses information from previous observations to learn temporal dependencies and generate future predictions.

### 4. LSTM (Long Short-Term Memory)

LSTM is an advanced recurrent neural network architecture designed to learn long-term dependencies in sequential data.

It uses memory cells and gating mechanisms to capture temporal patterns.

### 5. Facebook Prophet

Prophet is a time series forecasting model designed to capture trends, seasonal patterns and changes in time series data.

It is used to generate future earthquake activity forecasts.

##  7. Model Evaluation Metrics

The forecasting models are evaluated using three standard regression metrics.

| Metric | Full Form | Purpose |
|---|---|---|
| MAE | Mean Absolute Error | Measures average absolute prediction error |
| MSE | Mean Squared Error | Measures average squared prediction error |
| RMSE | Root Mean Squared Error | Measures prediction error in the original target unit |

### Evaluation Formulas

**Mean Absolute Error (MAE)**

MAE = (1/n) × Σ |Actual − Predicted|

**Mean Squared Error (MSE)**

MSE = (1/n) × Σ (Actual − Predicted)²

**Root Mean Squared Error (RMSE)**

RMSE = √MSE

Lower values generally indicate better forecasting performance.

##  8. Model Comparison

The project compares the performance of all five forecasting models.

Models are evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

The comparison results are stored in `comparison.csv`.

The dashboard provides visual comparisons to help identify the model with the best evaluation performance.

##  9. Future Forecasting

Each forecasting model generates predictions for the next five days.

The forecast results are stored separately:

- `arima.csv`
- `sarima.csv`
- `rnn.csv`
- `lstm.csv`
- `prophet.csv`

The dashboard allows users to select a forecasting model, view its predictions and download the forecast results.

## 🖥️ 10. Streamlit Dashboard

An interactive dashboard is developed using Streamlit and Plotly.

### Dashboard Modules

**1. Overview**
- Project summary.
- Historical earthquake record count.
- Daily observation count.
- Daily earthquake activity visualization.
- Model performance summary.

**2. Earthquake Analysis**
- Historical earthquake dataset.
- Magnitude distribution.
- Global earthquake geographical visualization.

**3. Model Comparison**
- Comparison of five forecasting models.
- MAE comparison.
- MSE comparison.
- RMSE comparison.

**4. Future Forecast**
- Model selection.
- Five-day future forecast.
- Forecast visualization.
- CSV download functionality.

**5. About Project**
- Project description.
- Forecasting models.
- Evaluation information.
- Project limitations.

##  11. Technologies and Libraries Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation |
| NumPy | Numerical computations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Statsmodels | ARIMA and SARIMA |
| TensorFlow / Keras | RNN and LSTM |
| Prophet | Time series forecasting |
| Scikit-learn | Data preprocessing and evaluation |
| Plotly | Interactive visualizations |
| Streamlit | Dashboard development |
| Google Colab | Model development and execution |
| GitHub | Version control and project hosting |
| Streamlit Community Cloud | Dashboard deployment |

##  12. Project Structure

```text
earthquake-forecasting-dashboard/
│
├── app.py
├── requirements.txt
├── README.md
│
├── historical.csv
├── combined.csv
├── daily.csv
├── comparison.csv
├── prophet_actual_vs_forecast.csv
│
├── arima.csv
├── sarima.csv
├── rnn.csv
├── lstm.csv
└── prophet.csv
```

##  13. Installation and Execution

### Step 1: Clone the Repository

```bash
git clone https://github.com/omswayzode2844/earthquake-forecasting-dashboard.git
```

### Step 2: Navigate to the Project Folder

```bash
cd earthquake-forecasting-dashboard
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit Application

```bash
streamlit run app.py
```

The dashboard will open in your browser.

##  14. Live Dashboard

**Streamlit Application:**

https://earthquake-forecasting-dashboard-pugcnumnhuwqhdujnikr.streamlit.app

##  15. Future Scope

The project can be enhanced through:

- Integration of continuously updated earthquake datasets.
- Automatic daily data collection.
- Longer forecasting horizons.
- Advanced deep learning architectures.
- Hyperparameter optimization.
- Additional statistical forecasting models.
- Improved geographical and temporal visualizations.
- Model retraining when new data becomes available.
- Monitoring forecast performance over time.

##  16. Limitations and Disclaimer

- The project forecasts aggregate daily earthquake counts, not individual earthquake events.
- Forecast results depend on the historical data and selected model configurations.
- Forecasts should not be interpreted as precise predictions of earthquake occurrence.
- The system cannot predict the exact time, location or magnitude of future earthquakes.
- This is an academic data science project and is not an earthquake early-warning system.

##  17. Author

**Om Wayzode**

M.Sc. Data Science

Savitribai Phule Pune University

### Project Domain
Time Series Analysis | Machine Learning | Deep Learning | Data Science

---

⭐ If you find this project interesting, consider giving the repository a star!
