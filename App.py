from flask import Flask, request, render_template, url_for
import yfinance as yf
import pandas as pd

from matplotlib.pylab import *
from werkzeug.utils import redirect

app = Flask(__name__)

data = pd.DataFrame({})


@app.route('/new/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


@app.route('/ticker/<symbol>', methods=(['GET']))
def tickerdata(symbol):
    data = yf.download(symbol, period='max', interval='1d')
    data.to_csv(symbol+'.csv')
    return data.to_html()


@app.route('/finance/', methods=(['POST','GET']))
def getTicker():
    if request.method == "POST":
        ticker = request.form['ticker']

        return redirect(url_for('tickerdata', symbol=ticker))
    else:
        # if the user refreshes the form by accident just re-render
        return render_template('YFinanceFrontEnd.html')


# our home route
@app.route('/')
def index():
    return render_template('YFinanceFrontEnd.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
