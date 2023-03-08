# Comp4447 project work 
## An interactive Yfinance based live ingestion application which can forecast stock data using ARIMA/SARIMA and Prophet API models. 
## Spotlight  Aaron for dockerizing application 
## Spotlight Bradley for SARIMA/ARIMA 
## Spotlight Kurt for prophet modeling 
## Spotlight Vivek for Flask Api integration

#### An interactive Flask based Web-App application that can predict using Arima/Sarima or Prophet the closing stock prices for any ticker of your choice


### To get started clone this repository in your personal workspace on your machine using `git clone https://github.com/vivekvaradarajan1980/Comp4447.git`

- Navigate into the directory where you clone this repository on your local machine

- Then install all the dependencies in the python requirements.txt using `pip install -r requirements.txt`

- Then run from your terminal 'flask run' or `python -i App.py`
(`flask run` opens the application in port 5000 which is the default but if you use `python -i App.py` it will run it in whatever port you configure it too in the App.py file. !!!)

- To run in Docker run "docker compose up -d" in your terminal (if you have port 5000 binded to something else you may have to change ports in the .yml)  

- Navigate to your browser to localhost:XXXX where XXXX is whatever port your application is running on.

## Data set and motivation
### Stock price forecasting using a web based application interface
## The idea is to make an interactive application that can be used to forecast stock price information for any chosen ticker symbol The forecasting model is trained on data using the current date to a certain time in history which is also a flexible parameter chosen by the user of the application. The forecasting duration is also a user customizable parameter in the application.
### Highlights of this project are 
- Yfinance for data ingestion
- Statsmodels and Prophet for data modeling
- Plotly for data visualization
- Flask for web api and 
- docker for containerizing the application

Useage of the application
- First the API gives the user an interface to choose a ticker symbol and the duration of data to train the model from current date
- Then the application shows an initial plot of the time series data of the chosen ticker sybmol for the duration selected along with the ADFueller test for stationarity.
- At this point, the user can pick a model for forecasting
- If Arima is chosen, the user will be presented with a PACF, ACF and first order difference. 
  1. At this point the user can make a best guess p,d,q estimate and enter a duration for forecasting can be entered in the input fields
  2. An additional seasonality option using the SARIMAX can be checked to account for any seasonal variations in the data.
- For Prophet, the beauty of the model is that it is absolutely automated and no parameters need be set except the duration of forecast required