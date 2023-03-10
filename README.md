# Comp4447 project work 
## An interactive Yfinance based live ingestion application which can forecast stock data using ARIMA/SARIMA and Prophet API models. 
## Spotlight  Aaron for dockerizing application 
## Spotlight Bradley for SARIMA/ARIMA 
## Spotlight Kurt for prophet modeling 
Facebook Prophet is an open-sourced tool available in Python or R that specifically helps with time-series forecasting. The motivation behind Prophet was to create something easy to use but customizable.  

Originally built to make predictions based on social media interactions, one of Prophet’s strengths is its ability to handle seasonal data. You can tailor your model for weekly, monthly, and yearly seasonal adjustments. Prophet can also adjust for holidays; you can even specify a specific country’s holiday schedule or add custom holidays. 

Prophet provides a collection of options in its models. These include uncertainty estimation, logistic vs linear regression, trend changepoints, and the ability to add regressors. Prophet also allows the user to run diagnostics. For example, you can run a rolling origin cross validation with customizable time options. 

The math behind the model is described in detail in Taylor SJ, Letham B. 2017. Forecasting at scale. PeerJ Preprints 5:e3190v2 https://doi.org/10.7287/peerj.preprints.3190v2. This article describes how Prophet incorporates a variety of linear models and smoothers to create a polished time-series forecasting tool. 

You can visit the Facebook Open-Source description of the project on GitHub to install or get additional information on how to use it.  The repository itself is also on GitHub. The links are below:

https://facebook.github.io/prophet/


https://github.com/facebook/prophet


## Spotlight Vivek for Flask Api integration

#### An interactive Flask based Web-App application for predicting closing stock prices using Arima/Sarima or Prophet for any ticker of your choice


### To get started clone this repository in your personal workspace on your machine using `git clone https://github.com/vivekvaradarajan1980/Comp4447.git`

- Navigate into the directory where you clone this repository on your local machine

- Then install all the dependencies in the python requirements.txt using `pip install -r requirements.txt`

- Then run from your terminal 'flask run' or `python -i App.py`
(`flask run` opens the application in port 5000 which is the default but if you use `python -i App.py` it will run it in whatever port you configure it too in the App.py file. !!!)

- To run in Docker run "docker compose up -d" in your terminal (if you have port 5000 binded to something else you may have to change ports in the .yml)  

- Navigate to your browser to localhost:XXXX where XXXX is whatever port your application is running on.

## Data set and motivation
### Stock price forecasting using an interactive web application
## The idea is to make an interactive application that can be used to forecast stock price information for any chosen ticker symbol The forecasting model is trained on data from the current date to a certain time in history which is a parameter chosen by the user. The forecasting duration is also a user customizable parameter in the application.
### Highlights of this project are 
- Yfinance for data ingestion
- Statsmodels and Prophet for data modeling
- Plotly for data visualization
- Flask for web api and 
- docker for containerizing the application

Useage of the application
- First the API gives the user an interface to choose a ticker symbol and the duration of data to train the model on from current date
- Then the application shows an initial plot of the time series data of the chosen ticker sybmol for the duration selected along with the ADFueller test for stationarity. A p-value less than 0.05 indicates that the data is stationary.
- At this point, the user can pick a model for forecasting
- If Arima is chosen, the user will be presented with a PACF, ACF and first order difference. 
  1. At this point the user can make a best guess p,d,q estimate and enter a duration for forecasting can be entered in the input fields
  2. An additional seasonality option using the SARIMAX can be checked to account for any seasonal variations in the data.
- For Prophet, the beauty of the model is that it is absolutely automated and no parameters need be set except the duration of forecast required. Although as mnentioned in [prophet](https://github.com/vivekvaradarajan1980/Comp4447/edit/main/README.md#spotlight-kurt-for-prophet-modeling) one can specify or account for specific holidays if there should be such a pattern in the data. 
