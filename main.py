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
time = pd.to_datetime('now', utc=True)
today = datetime.date.today()

# Get user input using streamlit widgets
def user_input_features():
    ticker = st.sidebar.text_input("Enter tickers saperated by commas: ", 'AAPL,AMZN,TSLA,NVDA,AMD')
    start_date = st.sidebar.date_input("Start Date", pd.to_datetime('2019-01-01'))
    end_date = st.sidebar.date_input("End Date", pd.to_datetime(today))
    return ticker, start_date, end_date

# Some basic opperations to assign date and split input string for symbol
symbol, start, end = user_input_features()
start = pd.to_datetime(start)
end = pd.to_datetime(end)
symbol = symbol.split(",")


# Read data
data = yf.download(symbol,start,end)


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