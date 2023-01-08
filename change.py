import yfinance as yf
import streamlit as st

# Get the ticker symbol from the user
ticker = st.text_input("Enter a ticker symbol:")

# Get the time frame and interval from the user
time_frame = st.selectbox("Select a time frame:", ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'])
interval = st.selectbox("Select an interval:", ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'])

# Get the stock data
data = yf.download(ticker, period=time_frame, interval=interval)

# Calculate the daily change in the 'Close' column
daily_change = data['Close'].pct_change()

# Calculate the hourly change in the 'Close' column
hourly_change = data['Close'].pct_change(periods=int(60/int(interval[:-1])))

# Calculate the minute change in the 'Close' column
minute_change = data['Close'].pct_change(periods=int(60/int(interval[:-1])))

# Display the daily, hourly, and minute change
st.write("Daily change:", daily_change)
st.write("Hourly change:", hourly_change)
st.write("Minute change:", minute_change)