import datetime
import streamlit as st
import pandas as pd
import yfinance as yf
import altair as alt
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components
import plotly.graph_objects as go
# from vega_datasets import data

APP_NAME = "Shab's Stock App"
a_interval = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
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

time = pd.to_datetime('now', utc=True)
today = datetime.date.today()
def user_input_features():
    ticker = st.sidebar.text_input("Enter tickers saperated by commas: ", 'AAPL,AMZN,TSLA,NVDA,AMD')
    start_date = st.sidebar.date_input("Start Date", pd.to_datetime('2019-01-01'))
    end_date = st.sidebar.date_input("End Date", pd.to_datetime(today))
    return ticker, start_date, end_date

symbol, start, end = user_input_features()

start = pd.to_datetime(start)
end = pd.to_datetime(end)

symbol = symbol.split(",")


# Read data
data = yf.download(symbol,start,end)

# df = pd.DataFrame(x, columns = x.feature_names)
# data.reset_index(inplace=True)
# data = pd.set_option('display.max_rows', None)

# df = pd.DataFrame(data)
# df = df.reset_index()
# fig = go.Line(df, x="Date")
# fig = go.Figure(
#     data=go.Scatter(x=df['Date'], y=df['Adj Close'])
# )
# fig.update_layout(
#     title={
#         'text': "Stock prices Over the period",
#         'y':0.9,
#         'x':0.5,
#         'xanchor': 'center',
#         'yanchor': 'top'
#     }
# )
# st.plotly_chart(fig, use_container_width=True)

ma = data.rolling(50).mean()

st.write("""## Price Chart""")
st.line_chart(data.Close)

st.write("""## Volume Chart""")
st.line_chart(data.Volume)

st.write("""## Moving Average Chart""")
st.line_chart(ma.Close)
st.write(data)

# fig = plt.figure()
# plt.plot(df.Close)
# fig_html = mpld3.fig_to_html(fig)
# components.html(fig_html, height=1600, width=1200)



# chart = alt.Chart(df).mark_line().encode(
#           y="Close")

# st.altair_chart(chart, use_container_width=True)




