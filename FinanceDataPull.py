import yfinance as yf
import pandas as pd
from matplotlib.pylab import  *

# pull data from specific ticker symbol over a specified period with a specified resolution interval
data = yf.download('IBM',period='730d',interval='1h')

#data index is basically date information...

plot(data.index,data['Close'])
show()