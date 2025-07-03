# China-Air-Pollution-Analysis

## Introduction

Here, we consider a [synthetic dataset](https://www.kaggle.com/datasets/khushikyad001/air-pollution-in-china-2015-2025/data) of air pollution and meteorological data for five cities in China: Shenzhen, Shanghai, Beijing, Chengdu, and Guangzhou. The data spans from 2015-2024. Our task is to forecast the air quality index (AQI) for each of these five cities from 2024 to 2030. Here, we use Auto-Regressive Integrated Moving Average (ARIMA), Exponential Time Series Smoothing (ETS), and Long Short-Term Memory (LSTM) models to produce time-series forecasts for AQI for each of the five cities in our dataset. My methodology is guided by [Jayita Gulati's post on ARIMA and LSTM for forecasting on Machine Learning Mastery](https://machinelearningmastery.com/mastering-time-series-forecasting-from-arima-to-lstm/).

## Contents

1. Data Pre-Processing
2. Descriptive Statistics for Each of Five Cities
3. Autoregressive Integrated Moving Average (ARIMA) AQI Forecast
4. Exponential Smoothing Time Series (ETS) AQI Forecast
5. Long Short-Term Memory (LSTM) Recurrent Neural Network (RNN) AQI Forecast
6. Conclusion

## (1)  Data Pre-Processing
