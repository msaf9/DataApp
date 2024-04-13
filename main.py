import datetime
import streamlit as st
from get_all_tickers import get_tickers as gt
# from get_all_tickers.get_tickers import Region
import yfinance as yf
import pandas as pd
st.set_page_config(page_title='Market Summary App', page_icon="📈", layout='centered', initial_sidebar_state='auto')

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.write("""
# Market Summary Application

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
    From = st.date_input("From", datetime.date(2020, 1, 1), min_value=None, max_value=None, key=None)
with col2:
    To = st.date_input("To", datetime.date.today(), min_value=None, max_value=None, key=None)

# Convert From and To dates to UTC timestamps
from_timestamp = datetime.datetime.combine(From, datetime.datetime.min.time()).timestamp()
to_timestamp = datetime.datetime.combine(To, datetime.datetime.min.time()).timestamp()

stockSymbol = stock
stockData = yf.Ticker(stockSymbol)
stockDf = stockData.history(period='1d', start=from_timestamp, end=to_timestamp)
st.line_chart(stockDf.Close)
st.line_chart(stockDf.Volume)

#x = st.slider('x')
#st.write(x, 'squared is', x * x)
