import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
# Stock Price Streamlit Application

Stock and volume over the time

""")

stock = st.selectbox(
'Which stock you would like to select?',
('AAPL', 'AMZN', 'GOOGL'))

st.write('You selected:', stock)

stockSymbol = stock
stockData = yf.Ticker(stockSymbol)
stockDf = stockData.history(period='1d', start='2011-10-10', end='2021-01-31')
st.line_chart(stockDf.Close)
st.line_chart(stockDf.Volume)

#x = st.slider('x')
#st.write(x, 'squared is', x * x)
