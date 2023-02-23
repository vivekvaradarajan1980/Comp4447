from urllib import request

import numpy as np
import pandas as pd
from plotly.subplots import make_subplots
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import pacf, acf
import plotly.graph_objects as go

def arima_analysis(data,p,d,q,duration):

    model = ARIMA(pd.Series(data['Close']), order=(p, d, q))
    fit=model.fit()
    fc= fit.get_forecast(duration) .summary_frame()
    upper_est=fc['mean_ci_upper']
    lower_est=fc['mean_ci_lower']
    mean_est=fc['mean']


    # Create Plotly plot of fitted values, predicted values and confidence interval range
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'].values, mode='lines', name='Actual;'))
    fig.add_trace(go.Scatter(x=data.index, y=fit.fittedvalues, mode='lines', name='Fitted'))
    fig.add_trace(go.Scatter(x=fc.index, y=mean_est, mode='lines', name='Predicted'))
    fig.add_trace(go.Scatter(x=fc.index, y=lower_est, mode='lines',line=dict(color='rgba(255,255,255,0)'),showlegend=False))
    fig.add_trace(go.Scatter(x=fc.index, y=upper_est, mode='lines',line=dict(color='rgba(255,255,255,0)'),fill='tonexty', fillcolor='rgba(0, 0, 255, 0.2)'
                            , showlegend=False))
    fig.update_layout(title='ARIMA Forecasts with Confidence Intervals', xaxis_title='day, index',
                      yaxis_title='Closing values')
    return fig




def arima_figures(data):
    df_pacf = pacf(data['Close'], nlags=30)
    df_acf = acf(data['Close'], nlags=30)
    fig = make_subplots(rows=1, cols=3)
    fig.add_trace(go.Scatter(
        x=np.arange(len(df_pacf)),
        y=df_pacf,
        name='PACF',
    ), row=1, col=1)
    fig.add_trace(go.Scatter(
        x=np.arange(len(df_acf)),
        y=df_acf,
        name='ACF',
    ), row=1, col=2)
    fig.add_trace(go.Scatter(x=np.arange(len(data) - 1), y=np.diff(data.Close.values), name='1st difference'), row=1,
                  col=3)
    fig['layout']['xaxis']['title'] = 'Lags'
    fig['layout']['yaxis']['title'] = 'PACF'
    return fig