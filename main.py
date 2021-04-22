import streamlit as st
from get_all_tickers import get_tickers as gt
from get_all_tickers.get_tickers import Region
import yfinance as yf
import pandas as pd

st.write("""
# Stock Price Streamlit Application

Stock and volume over the time

""")
pd.set_option("display.max_rows", None, "display.max_columns", None)
df = pd.read_csv('symbols.csv')
df1 = df[['symbol']]
result = df1.head(None)
print(result)

stock = st.selectbox(
'Which stock you would like to select?',
(result))

stock_name = df.loc[df['symbol'] == stock, 'name'].iloc[0]
# name = stock_name.head(None)
st.write('You selected:', stock_name)

stockSymbol = stock
stockData = yf.Ticker(stockSymbol)
stockDf = stockData.history(period='1d', start='2011-10-10', end='2021-01-31')
st.line_chart(stockDf.Close)
st.line_chart(stockDf.Volume)

#x = st.slider('x')
#st.write(x, 'squared is', x * x)
