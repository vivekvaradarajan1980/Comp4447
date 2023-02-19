def sarimax_analysis(data,p,d,q,P,D,Q,s,duration):
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
    import pandas as pd
    import statsmodels.api as sm
    
    model=sm.tsa.SARIMAX(pd.Series(data["Close"].values),order=(p,d,q),
                        seasonal_order=(P,D,Q,s))
    fit=model.fit()
    fc= fit.get_forecast(duration) .summary_frame()

    return fit, fc
