import datetime
import yfinance as yf
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# --- Page Config ---
st.set_page_config(page_title="📊 Stock Price App", layout="wide")

# --- App Title ---
st.markdown("""
    <h1 style="color:#4CAF50; text-align:center;">
        📈 Real-Time Stock Price & Chart View
    </h1>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Ticker Input ---
st.sidebar.header("🔎 Stock Ticker & Date Range")
ticker_symbol = st.sidebar.text_input("Enter Stock Ticker Symbol (e.g. AAPL)", "AAPL").upper()

# --- Date Range with Defaults ---
today = datetime.date.today()
default_start = today - datetime.timedelta(days=30)

start_date = st.sidebar.date_input("Start Date", default_start)
end_date = st.sidebar.date_input("End Date", today)

# --- Fetch Data ---
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period="1d", start=start_date, end=end_date)

# --- Validate Data ---
if ticker_df.empty:
    st.error("⚠️ No data found. Check your stock ticker or date range.")
    st.stop()

# --- Add Moving Averages ---
ticker_df['SMA20'] = ticker_df['Close'].rolling(window=20).mean()
ticker_df['SMA50'] = ticker_df['Close'].rolling(window=50).mean()

# --- Expandable Raw Data ---
with st.expander("📊 View Raw Data", expanded=False):
    st.dataframe(ticker_df)

# --- Charts Section ---
st.markdown("## 📉 Price Trends & Candlestick Chart")

col1, col2 = st.columns(2)

# --- Line Chart: Close with SMAs ---
with col1:
    st.subheader(f"{ticker_symbol} Closing Price (with SMA20 & SMA50)")
    st.line_chart(ticker_df[['Close', 'SMA20', 'SMA50']])

# --- Line Chart: Volume ---
with col2:
    st.subheader(f"{ticker_symbol} Volume")
    st.line_chart(ticker_df['Volume'])

# --- Candlestick Chart ---
st.markdown("## 🕯️ Interactive Candlestick Chart")

fig = go.Figure(data=[go.Candlestick(
    x=ticker_df.index,
    open=ticker_df['Open'],
    high=ticker_df['High'],
    low=ticker_df['Low'],
    close=ticker_df['Close'],
    increasing_line_color='green',
    decreasing_line_color='red'
)])

fig.update_layout(
    title=f"{ticker_symbol} Candlestick Chart",
    xaxis_title="Date",
    yaxis_title="Price",
    template="plotly_dark",
    xaxis_rangeslider_visible=True,
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=7, label="1W", step="day", stepmode="backward"),
                dict(count=1, label="1M", step="month", stepmode="backward"),
                dict(count=3, label="3M", step="month", stepmode="backward"),
                dict(step="all", label="All")
            ])
        ),
        rangeslider=dict(visible=True),
        type="date"
    )
)

st.plotly_chart(fig, use_container_width=True)

# --- Footer ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: grey;'>Built with ❤️ using Streamlit, yFinance, and Plotly</p>",
    unsafe_allow_html=True
)
# --- End of App ---
# This code is a complete Streamlit app that allows users to view real-time stock prices and charts.
# It includes features like moving averages, candlestick charts, and an expandable raw data view.
# The app is designed to be user-friendly and visually appealing, with a focus on providing valuable insights into stock performance.   
