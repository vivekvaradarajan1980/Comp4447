import pandas as pd
import plotly.express as px
import yfinance as yf
from flask import Flask, request, render_template, url_for
from prophet import Prophet
import plotly.graph_objects as go
from statsmodels.tsa.stattools import adfuller
from werkzeug.utils import redirect

from Arima import arima_analysis, arima_figures
from ProphetAPI import prophet_analysis
from Sarimax import sarimax_analysis

app = Flask(__name__)

global data  # we will use this to extract the data from yfinance and consume it in our endpoints
data = pd.DataFrame({})
global years

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    global data

    fig=px.line(data, x=data.index, y=data['Close'])
    """
   Returns plot and 2 buttons to choose which model we want to look at 
    """
    result = adfuller(data['Close'])

    return fig.to_html()+ str("AdFuller test for stationarity")+str(result)+render_template('Choose_model.html')


@app.route('/summary/', methods=['GET', 'POST'])
def summary():
    return redirect("https://finance.yahoo.com/lookup/")


@app.route('/ticker/<symbol>', methods=(['GET']))
def tickerdata(symbol):
    global data
    global years

    data = yf.download(symbol, period=years+"y", interval='1d')
    if (data.empty != True):

        return "<a href=/prediction>Further insights into your chosen stock</a><br/></br>" +data.to_html()
    else:
        return render_template('YFinanceFrontEnd.html')


@app.route('/finance/', methods=(['POST', 'GET']))
def getTicker():
    if request.method == "POST":
        ticker = request.form['ticker']
        global years
        years=request.form['history']

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
    fig = arima_figures(data)

    return fig.to_html()+render_template('arima.html')





@app.route('/arimamodel',methods=(['POST','GET']))
def arima_prediction():
    global data
    try:
        p = int(request.form['p'])
        d = int(request.form['d'])
        q = int(request.form['q'])
        no_args=0
    except:
        no_args=1

    sarima = request.form.get('sarima')
    try:
        duration = int(request.form['duration'])
    except:
        duration=14

    if(sarima and no_args==0):
        fig = sarimax_analysis(data,duration,p,d,q,p,d,q,4)
    elif(sarima and no_args==1):
        fig = sarimax_analysis(data,duration)
    else:
        fig = arima_analysis(data,p,d,q,duration)


    return fig.to_html()+render_template('arima.html')

@app.route('/prophet',methods=(['POST','GET']))
def prophet_prediction():
    global data
    fig = prophet_analysis(data,int(request.form['duration']))

    return fig.to_html()+render_template('Choose_model.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
