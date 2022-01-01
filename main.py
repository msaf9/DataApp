import streamlit as st
from get_all_tickers import get_tickers as gt
# from get_all_tickers.get_tickers import Region
import yfinance as yf
import pandas as pd
st.set_page_config(page_title='Stock Data App', page_icon="📈", layout='centered', initial_sidebar_state='auto')

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.write("""
# Stock Data Application

Stock and volume over the time

""")
pd.set_option("display.max_rows", None, "display.max_columns", None)
df = pd.read_csv('symbols.csv')
df1 = df[['symbol']]
result = df1.head(None)
# result.to_csv('tickers.csv') 
# print(result)

stock = st.selectbox(
'Which stock you would like to select?',
(result))

stock_name = df.loc[df['symbol'] == stock, 'name'].iloc[0]
# name = stock_name.head(None)
st.write('You have selected:', stock_name)

col1, col2 = st.columns(2)
with col1:
    From = st.date_input("From", value=None, min_value=None, max_value=None, key=None)
with col2:
    To = st.date_input("To", value=None, min_value=None, max_value=None, key=None)

stockSymbol = stock
stockData = yf.Ticker(stockSymbol)
stockDf = stockData.history(period='1d', start=From, end=To)
st.line_chart(stockDf.Close)
st.line_chart(stockDf.Volume)

#x = st.slider('x')
#st.write(x, 'squared is', x * x)
