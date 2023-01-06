# Libraries required for application
import datetime
import streamlit as st
import pandas as pd
import yfinance as yf

# App Info
APP_NAME = "Shab's Stock App"
ticker = []

# Page Configuration
st.set_page_config(
    page_title=APP_NAME,
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add some markdown
st.write("""
# Stock & Forex Data Visualization application using Streamlit """)
st.sidebar.header('User Input Parameters  :chart_with_upwards_trend:')

# Get time for calander widget
# time = pd.to_datetime('now', utc=True)
# today = datetime.date.today()

# Get user input using streamlit widgets
def user_input_features():
    ticker = st.sidebar.text_input("Enter tickers saperated by commas: ", 'AAPL,AMZN,TSLA,NVDA,AMD')
    # start_date = st.sidebar.date_input("Start Date", pd.to_datetime('2019-01-01'))
    # end_date = st.sidebar.date_input("End Date", pd.to_datetime(today))
    # Get the time frame and interval from the user
    time_frame = st.sidebar.selectbox("Select a time frame:", ['1d', '5d', '7d', '14d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'])
    interval = st.sidebar.selectbox("Select an interval:", ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'])
    return ticker, time_frame, interval

# Some basic opperations to assign date and split input string for symbol
symbol, time_frame, interval = user_input_features()
symbol = symbol.split(",")


# Read data
data = yf.download(symbol,period =time_frame,interval=interval)


# Calculate Moving Average 
ma = data.rolling(50).mean()


#Plot Chart for price
st.write("""## Price Chart""")
st.line_chart(data.Close)

#Plot Chart for Volume
st.write("""## Volume Chart""")
st.line_chart(data.Volume)

#Plot Chart for Moving Average
st.write("""## Moving Average Chart""")
st.line_chart(ma.Close)
st.write(data)