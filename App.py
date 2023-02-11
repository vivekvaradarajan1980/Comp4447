import io
import json

import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from flask import Flask, request, render_template, url_for, Response
import yfinance as yf
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg
from statsmodels.graphics.tsaplots import pacf,acf
from matplotlib.pylab import Figure
import plotly.express as px
import plotly.graph_objects as go

from werkzeug.utils import redirect

app = Flask(__name__)

global data  # we will use this to extract the data from yfinance and consume it in our endpoints
data = pd.DataFrame({})


@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    global data

    fig=px.line(data, x=data.index, y=data['Close'])
    """
   Returns plot and 2 buttons to choose which model we want to look at 
    """
    return fig.to_html()+render_template('Choose_model.html')


@app.route('/summary/', methods=['GET', 'POST'])
def summary():
    return redirect("https://finance.yahoo.com/lookup/")


@app.route('/ticker/<symbol>', methods=(['GET']))
def tickerdata(symbol):
    global data
    data = yf.download(symbol, period='max', interval='1d')
    if (data.empty != True):

        return "<a href=/prediction>Further insights into your chosen stock</a><br/></br>" +data.to_html()
    else:
        return render_template('YFinanceFrontEnd.html')


@app.route('/finance/', methods=(['POST', 'GET']))
def getTicker():
    if request.method == "POST":
        ticker = request.form['ticker']

        return redirect(url_for('tickerdata', symbol=ticker.upper()))
    else:
        # if the user refreshes the form by accident just re-render
        return render_template('YFinanceFrontEnd.html')


# our home route
@app.route('/')
def index():
    return render_template('YFinanceFrontEnd.html')


@app.route('/arimadiagnostics',methods=(['POST','GET']))
def arima():
    global data
    df_pacf = pacf(data['Close'], nlags=30)

    fig=go.Figure()
    fig.add_trace(go.Scatter(
        x=np.arange(len(df_pacf)),
        y=df_pacf,
        name='PACF',
    ))

    fig.add_trace(go.Scatter(x=np.arange(len(data)-1),y=np.diff(data.Close.values),name='1st difference'))


    return fig.to_html()+render_template('arima.html')


@app.route('/arimaanalysis',methods=(['POST','GET']))
def arima_prediction():
    """ do the stuff with arima here and show results"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
