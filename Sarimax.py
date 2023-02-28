import statsmodels.api as sm
import pandas as pd
import plotly.graph_objects as go

def sarimax_analysis(data,duration,p=1,d=1,q=1,P=1,D=1,Q=1,s=4):
    """
    model similar to arima but good for stocks that are more seasonal.
    0, 1 and 2 are good values for p,d,q if you don't know what to pick.
    s is usually 4 or 12.
    
    Args:
    
      p: how many previous data points should be used from auto regressive model
      d: how many times data is to be differenced
      q: how many previous data points should be used from moving average model
      P,D,Q: same as p,d,q but for the seasonal period rather than the full data
      s: time period of the model, for example 4 would be seasonal, 12 would be monthly 
      duration: how many days in the future the model predicts
      
    Returns:
    
      (fit, fc): tuple containing fit object returned by the model fit and forecast data.
      
    Example:
    
      >>> (fit, fc) = sarimax_analysis(data, p= 2, d= 1,q= 1, s= 4, P= 1, D= 1, Q= 1, duration= 3)
    """

    model=sm.tsa.SARIMAX(data["Close"],order=(p,d,q),
                        seasonal_order=(P,D,Q,s))
    fit=model.fit()
    fc= fit.get_forecast(duration) .summary_frame()
    fc.index = pd.date_range(data.index[-1].date(), periods=duration)
    upper_est = fc['mean_ci_upper']
    lower_est = fc['mean_ci_lower']
    mean_est = fc['mean']

    # Create Plotly plot of fitted values, predicted values and confidence interval range
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'].values, mode='lines', name='Actual;'))
    fig.add_trace(go.Scatter(x=data.index, y=fit.fittedvalues, mode='lines', name='Fitted'))
    fig.add_trace(go.Scatter(x=fc.index, y=mean_est, mode='lines', name='Predicted'))
    fig.add_trace(
        go.Scatter(x=fc.index, y=lower_est, mode='lines', line=dict(color='rgba(255,255,255,0)'), showlegend=False))
    fig.add_trace(
        go.Scatter(x=fc.index, y=upper_est, mode='lines', line=dict(color='rgba(255,255,255,0)'), fill='tonexty',
                   fillcolor='rgba(0, 0, 255, 0.2)'
                   , showlegend=False))
    fig.update_layout(title='ARIMA Forecasts with Confidence Intervals', xaxis_title='date',
                      yaxis_title='Closing values')
    return fig


