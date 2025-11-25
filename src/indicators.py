import talib
import pandas as pd

def add_technical_indicators(df, close_col='Close'):
   """
   Adds common technical indicators to a stock DataFrame.
   Parameters:
       df (pd.DataFrame): Stock DataFrame containing a 'Close' column.
       close_col (str): Name of the closing price column (default: 'Close').
   Returns:
       pd.DataFrame: DataFrame with added columns: SMA_20, EMA_20, RSI_14, MACD, MACD_signal, MACD_hist.
   """
   df = df.copy()  # avoid modifying original df
   # Simple Moving Average (SMA) for 20 days
   df['SMA_20'] = talib.SMA(df[close_col], timeperiod=20)
   # Exponential Moving Average (EMA) for 20 days
   df['EMA_20'] = talib.EMA(df[close_col], timeperiod=20)
   # RSI for 14 days
   df['RSI_14'] = talib.RSI(df[close_col], timeperiod=14)
   # MACD (12, 26, 9)
   df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(
       df[close_col], fastperiod=12, slowperiod=26, signalperiod=9
   )
   return df