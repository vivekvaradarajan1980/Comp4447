import yfinance as yf
import pandas as pd
from matplotlib.pylab import *
import argparse
from statsmodels.graphics.tsaplots import plot_acf

# pull data from specific ticker symbol over a specified period with a specified resolution interval

parser = argparse.ArgumentParser(
    prog="Stock information",
    description="Uses yfinance library to get financial data from different ticker symbols",
)


parser.add_argument("-t", "--ticker", type=str, required=False, default="GOOG")
parser.add_argument("-o", "--option", type=str, required=False, default="Close")
parser.add_argument("-p", "--period", type=str, required=False, default="2y")
parser.add_argument("-v", "--interval", type=str, required=False, default="1d")



ticker = parser.parse_args().ticker
option = parser.parse_args().option
period = parser.parse_args().period
interval = parser.parse_args().interval
data = yf.download(ticker, period=period, interval=interval)

# data index is basically date information...

plot(data.index, data[option])
show()
