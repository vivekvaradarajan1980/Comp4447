import pandas as pd
from prophet import Prophet
import plotly.graph_objects as go


def prophet_analysis(data, duration=14):
    data.reset_index(inplace=True)
    df1 = data[['Date', 'Close']]
    # Convert the date column to datetime
    df1['Date'] = pd.to_datetime(df1['Date'])
    df1['Date'] = df1['Date'].dt.tz_localize(None)
    df1 = df1.rename(columns={"Date": "ds", "Close": "y"})
    m = Prophet(daily_seasonality=True)
    m.fit(df1)
    future = m.make_future_dataframe(periods=duration)
    forecast = m.predict(future)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df1['ds'], y=df1['y'], name='Actual'))
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], name='Predicted'))

    return fig
