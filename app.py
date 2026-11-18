
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os

# Project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# CSV files are stored in the root directory
DATA = BASE_DIR


def load_csv(filename):
    path = os.path.join(DATA, filename)

    if os.path.exists(path):
        return pd.read_csv(path)

    return None

historical = load_csv("historical.csv")
daily = load_csv("daily.csv")
comparison = load_csv("comparison.csv")

models = {
    "ARIMA": load_csv("arima.csv"),
    "SARIMA": load_csv("sarima.csv"),
    "RNN": load_csv("rnn.csv"),
    "LSTM": load_csv("lstm.csv"),
    "Prophet": load_csv("prophet.csv")
}

st.title("🌍 Global Earthquake Analysis & Forecasting")
st.markdown("### Time Series Forecasting using Five Models")

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Earthquake Analysis",
        "Model Comparison",
        "Future Forecast",
        "About"
    ]
)

if page == "Overview":

    st.header("Project Overview")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Historical Records",
        len(historical) if historical is not None else 0
    )

    c2.metric(
        "Daily Observations",
        len(daily) if daily is not None else 0
    )

    c3.metric("Forecasting Models", 5)

    if daily is not None:
        count_col = "earthquake_count"

        if count_col in daily.columns:
            date_col = daily.columns[0]

            daily[date_col] = pd.to_datetime(
                daily[date_col], errors="coerce"
            )

            fig = px.line(
                daily,
                x=date_col,
                y=count_col,
                title="Daily Earthquake Activity"
            )

            st.plotly_chart(fig, use_container_width=True)

    st.subheader("Model Performance")

    if comparison is not None:
        st.dataframe(comparison, use_container_width=True)
    else:
        st.warning("Comparison file not found.")

elif page == "Earthquake Analysis":

    st.header("Earthquake Data Analysis")

    if historical is not None:

        st.subheader("Historical Dataset")
        st.dataframe(historical.head(100))

        if "mag" in historical.columns:
            fig = px.histogram(
                historical,
                x="mag",
                nbins=40,
                title="Earthquake Magnitude Distribution"
            )
            st.plotly_chart(fig, use_container_width=True)

        if {"latitude", "longitude"}.issubset(historical.columns):

            map_data = historical.copy()

            map_data["latitude"] = pd.to_numeric(
                map_data["latitude"], errors="coerce"
            )
            map_data["longitude"] = pd.to_numeric(
                map_data["longitude"], errors="coerce"
            )

            map_data = map_data.dropna(
                subset=["latitude", "longitude"]
            )

            fig = px.scatter_geo(
                map_data,
                lat="latitude",
                lon="longitude",
                color="mag" if "mag" in map_data.columns else None,
                hover_name="place" if "place" in map_data.columns else None,
                title="Global Earthquake Locations"
            )

            st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("Historical dataset not found.")

elif page == "Model Comparison":

    st.header("Five Model Performance Comparison")

    if comparison is not None:

        st.dataframe(comparison, use_container_width=True)

        if "Model" in comparison.columns:

            for metric in ["MAE", "MSE", "RMSE"]:

                if metric in comparison.columns:

                    fig = px.bar(
                        comparison,
                        x="Model",
                        y=metric,
                        title=f"Model Comparison - {metric}",
                        text_auto=True
                    )

                    st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("Model comparison file not found.")

elif page == "Future Forecast":

    st.header("Five-Day Future Forecast")

    selected_model = st.selectbox(
        "Select Forecasting Model",
        list(models.keys())
    )

    forecast = models[selected_model]

    if forecast is not None:

        st.subheader(f"{selected_model} Forecast")

        st.dataframe(forecast, use_container_width=True)

        date_col = next(
            (c for c in forecast.columns if c.lower() == "date"),
            None
        )

        value_col = next(
            (
                c for c in forecast.columns
                if "predicted" in c.lower()
            ),
            None
        )

        if date_col and value_col:

            fig = px.line(
                forecast,
                x=date_col,
                y=value_col,
                markers=True,
                title=f"{selected_model} Future Forecast"
            )

            st.plotly_chart(fig, use_container_width=True)

        st.download_button(
            "Download Forecast CSV",
            forecast.to_csv(index=False),
            file_name=f"{selected_model.lower()}_forecast.csv",
            mime="text/csv"
        )

    else:
        st.error(f"{selected_model} forecast CSV is missing.")

elif page == "About":

    st.header("About the Project")

    st.write("""
    This project analyzes global earthquake activity using
    historical data from the USGS Earthquake Catalog.

    Forecasting models:

    1. ARIMA
    2. SARIMA
    3. Recurrent Neural Network (RNN)
    4. Long Short-Term Memory (LSTM)
    5. Facebook Prophet

    Evaluation metrics:

    - MAE
    - MSE
    - RMSE

    Disclaimer: This project forecasts aggregate earthquake
    activity. It does not predict the exact time, location or
    magnitude of individual earthquakes and is not an
    earthquake early-warning system.
    """)

st.sidebar.markdown("---")
st.sidebar.caption("M.Sc. Data Science Project")
