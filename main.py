import pandas as pd
import numpy as np
import datetime
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ochl

# creating a dictionary
dict_={'a':[0,1,2], 'b':[3,4,5]}
df = pd.DataFrame(dict_)

# setting instance to API
cg = CoinGeckoAPI()

# storing btc market data for last 30 days in canadian dollar
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency="cad", days=30)

# getting bitcoin price data
bitcoin_price_data = bitcoin_data['prices']

# turning data to pandas dataframe
data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])

# converting timestamp to datetime and saving as date column
data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))

# group by date to find min, max, open, close
candlestick_data = data.groupby(data.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})

# creating candlestick chart
fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
                open=candlestick_data['Price']['first'],
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'],
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()








