import ccxt
from datetime import datetime
import pandas
import matplotlib.pyplot as plt

# collect the candlestick data from Luno
luno = ccxt.luno()
trading_pair = 'BTC/EUR'
candles = luno.fetch_ohlcv(trading_pair, '1h')

dates = []
open_data = []
high_data = []
low_data = []
close_data = []

# format the data to match the charting library
for candle in candles:
    dates.append(datetime.fromtimestamp(candle[0] / 1000.0))
    open_data.append(candle[1])
    high_data.append(candle[2])
    low_data.append(candle[3])
    close_data.append(candle[4])

#plt.plot(dates,open_data)
#plt.plot(dates,close_data)
plt.plot(dates,low_data)
plt.plot(dates,high_data)
plt.show()
