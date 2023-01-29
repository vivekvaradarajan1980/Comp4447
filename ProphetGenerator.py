import yfinance as yf
import pandas as pd
from matplotlib.pylab import *
import argparse
from statsmodels.graphics.tsaplots import plot_acf
from prophet import Prophet

# pull data from specific ticker symbol over a specified period with a specified resolution interval

parser = argparse.ArgumentParser(
    prog="Stock information",
    description="Uses yfinance library to get financial data from different ticker symbols",
)


parser.add_argument("-t", "--ticker", type=str, required=False, default="AAPL")
parser.add_argument("-o", "--option", type=str, required=False, default="Close")
parser.add_argument("-p", "--period", type=str, required=False, default="2y")
parser.add_argument("-v", "--interval", type=str, required=False, default="1d")



ticker = parser.parse_args().ticker
option = parser.parse_args().option
period = parser.parse_args().period
interval = parser.parse_args().interval
data = yf.download(ticker, period=period, group_by='column', interval=interval)

# Resetting index so dates can be used. 
data.reset_index(inplace=True)
df1=data[['Date', 'Close']]

# Convert the date column to datetime
df1['Date'] = pd.to_datetime(df1['Date'])

# Remove the time zone information
df1['Date'] = df1['Date'].dt.tz_localize(None)
#Rename columns for Prophet requirements
df1=df1.rename(columns = {"Date": "ds", "Close": "y"})
print(df1)

#Create prophet object
m = Prophet()
m.fit(df1)  #Meta Magic

#Future predictions

future = m.make_future_dataframe(periods = 14)

x = m.predict(future)

y = m.plot(x)


