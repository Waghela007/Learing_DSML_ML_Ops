import datetime
import yfinance as yf
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


st.title(" Stock Price App" + " 📈")

ticker_symbol = st.text_input("Enter Stock Ticker Symbol", "AAPL")

ticker_data = yf.Ticker(ticker_symbol)

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date")
with col2:
    end_date = st.date_input("End Date")

ticker_df = ticker_data.history(period="1d", start= start_date, end= end_date)

st.dataframe(ticker_df)
col1, col2 = st.columns(2)
with col1:
    st.write(f"**{ticker_symbol} Stock Closing Price**")
with col2:
    st.write(f"**{ticker_symbol} Stock Volume**")

with col1:
    st.line_chart(ticker_df.Close, x_label="Date", y_label="Closing Price",color=["#fd0"])
with col2:
    st.line_chart(ticker_df.Volume, x_label="Date", y_label="Volume")

data = ticker_df
fig = go.Figure(data=[go.Candlestick(
    x=ticker_df.index,
    open=ticker_df['Open'],
    high=ticker_df['High'],
    low=ticker_df['Low'],
    close=ticker_df['Close']
)])
fig.update_layout(
    title=f'{ticker_symbol} Candlestick Chart',
    xaxis_title='Date',
    yaxis_title='Price',
    xaxis_rangeslider_visible=False
)
st.plotly_chart(fig, use_container_width=True)


