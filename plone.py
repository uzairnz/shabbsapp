import yfinance as yf
import streamlit as st

# Get the ticker symbol from the user
ticker = st.text_input("Enter a ticker symbol:")

# Get the time frame and interval from the user
time_frame = st.selectbox("Select a time frame:", ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'])
interval = st.selectbox("Select an interval:", ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'])

# Get the stock data
data = yf.download(ticker, period=time_frame, interval=interval)

# Calculate the 50-day moving average
data['ma'] = data['Adj Close'].rolling(50).mean()

# Plot the 'Adj Close' column and the moving average on the same graph
st.line_chart(data[['Adj Close', 'ma']])