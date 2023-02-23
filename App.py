import pandas as pd
import plotly.express as px
import yfinance as yf
from flask import Flask, request, render_template, url_for
from prophet import Prophet
import plotly.graph_objects as go
from werkzeug.utils import redirect

from Arima import arima_analysis, arima_figures
from ProphetAPI import prophet_analysis

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
    data = yf.download(symbol, period='5y', interval='1d')
    data["Date"] = data.index
    data.reset_index(drop=True, inplace=True)
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
    fig = arima_figures(data)

    return fig.to_html()+render_template('arima.html')





@app.route('/analysis',methods=(['POST','GET']))
def arima_prediction():
    global data
    p = int(request.form['p'])
    d = int(request.form['d'])
    q = int(request.form['q'])
    duration = int(request.form['duration'])
    fig = arima_analysis(data,p,d,q,duration)

    return fig.to_html()+render_template('arima.html')

@app.route('/prophet',methods=(['POST','GET']))
def prophet_prediction():
    global data
    fig = prophet_analysis(data,int(request.form['duration']))

    return fig.to_html()+render_template('Choose_model.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
