import yfinance as yf
import pandas as pd
from matplotlib.pylab import  *
import argparse

# pull data from specific ticker symbol over a specified period with a specified resolution interval

parser = argparse.ArgumentParser(
                    prog = 'Stock information',
                    description = 'Plots closing stock over last 2 years with 1 hour resolution'
                    )


parser.add_argument('-t','--ticker',type=str,required=False, default="GOOG")
parser.add_argument('-o','--option',type=str,required=False,default="Close")


ticker= parser.parse_args().ticker
option = parser.parse_args().option

data = yf.download(ticker,period='730d',interval='1h')

#data index is basically date information...

plot(data.index,data[option])
show()