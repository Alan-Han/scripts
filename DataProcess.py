import sys
sys.path.append('..')

import pandas as pd
import talib
raw_data = pd.read_csv('1minutekrakenUSD14--190731.csv')

# 删除Adj Close列
raw_data.pop('Adj Close')

# 加入MACD数据 TODO：加入金叉死叉
macd_tmp = talib.MACD(raw_data["Close"], 12, 26, 20)
raw_data['MACD'] = macd_tmp[0]
raw_data['SIGNAL'] = macd_tmp[1]
raw_data['HIST'] = macd_tmp[2]

# 加入MA数据
ema5_tmp = talib.EMA(raw_data['Close'], timeperiod=5)
ema15_tmp = talib.EMA(raw_data['Close'], timeperiod=15)
ema100_tmp = talib.EMA(raw_data['Close'], timeperiod=100)
ema300_tmp = talib.EMA(raw_data['Close'], timeperiod=300)
# ema900_tmp = talib.EMA(raw_data['Close'], timeperiod=900)
# ema1800_tmp = talib.EMA(raw_data['Close'], timeperiod=1800)  # 1h
# ema5400_tmp = talib.EMA(raw_data['Close'], timeperiod=5400)  # 3h
# ema10800_tmp = talib.EMA(raw_data['Close'], timeperiod=10800)  # 6h
# ema21600_tmp = talib.EMA(raw_data['Close'], timeperiod=21600)  # 12h
# ema43200_tmp = talib.EMA(raw_data['Close'], timeperiod=43200)  # 1d
# ema129600_tmp = talib.EMA(raw_data['Close'], timeperiod=129600)  # 3d
# ema302400_tmp = talib.EMA(raw_data['Close'], timeperiod=302400)  # 7d
# ema1209600_tmp = talib.EMA(raw_data['Close'], timeperiod=1209600)  # 1M
raw_data['EMA11'] = ema5_tmp
raw_data['EMA22'] = ema15_tmp
raw_data['EMA100'] = ema100_tmp
raw_data['EMA300'] = ema300_tmp
# raw_data['EMA900'] = ema900_tmp
# raw_data['EMA1800'] = ema1800_tmp
# raw_data['EMA5400'] = ema5400_tmp
# raw_data['EMA10800'] = ema10800_tmp
# raw_data['EMA21600'] = ema21600_tmp
# raw_data['EMA43200'] = ema43200_tmp
# raw_data['EMA129600'] = ema129600_tmp
# raw_data['EMA302400'] = ema302400_tmp
# raw_data['EMA1209600'] = ema129600_tmp

# 加入RSI数据
rsi5_tmp = talib.RSI(raw_data['Close'], timeperiod=5)
rsi15_tmp = talib.RSI(raw_data['Close'], timeperiod=15)
rsi100_tmp = talib.RSI(raw_data['Close'], timeperiod=100)
rsi300_tmp = talib.RSI(raw_data['Close'], timeperiod=300)
# rsi900_tmp = talib.RSI(raw_data['Close'], timeperiod=900)
# rsi1800_tmp = talib.RSI(raw_data['Close'], timeperiod=1800)  # 1h
# rsi5400_tmp = talib.RSI(raw_data['Close'], timeperiod=5400)  # 3h
# rsi10800_tmp = talib.RSI(raw_data['Close'], timeperiod=10800)  # 6h
# rsi21600_tmp = talib.RSI(raw_data['Close'], timeperiod=21600)  # 12h
# rsi43200_tmp = talib.RSI(raw_data['Close'], timeperiod=43200)  # 1d
# rsi129600_tmp = talib.RSI(raw_data['Close'], timeperiod=129600)  # 3d
# rsi302400_tmp = talib.RSI(raw_data['Close'], timeperiod=302400)  # 7d
# rsi1209600_tmp = talib.RSI(raw_data['Close'], timeperiod=1209600)  # 1M
raw_data['RSI5'] = rsi5_tmp
raw_data['RSI15'] = rsi15_tmp
raw_data['RSI100'] = rsi100_tmp
raw_data['RSI300'] = rsi300_tmp
# raw_data['RSI900'] = rsi900_tmp
# raw_data['RSI1800'] = rsi1800_tmp
# raw_data['RSI5400'] = rsi5400_tmp
# raw_data['RSI10800'] = rsi10800_tmp
# raw_data['RSI21600'] = rsi21600_tmp
# raw_data['RSI43200'] = rsi43200_tmp
# raw_data['RSI129600'] = rsi129600_tmp
# raw_data['RSI302400'] = rsi302400_tmp
# raw_data['RSI1209600'] = rsi129600_tmp

# 加入MOM数据
mom5_tmp = talib.MOM(raw_data['Close'], timeperiod=5)
mom15_tmp = talib.MOM(raw_data['Close'], timeperiod=15)
mom100_tmp = talib.MOM(raw_data['Close'], timeperiod=100)
mom300_tmp = talib.MOM(raw_data['Close'], timeperiod=300)
# mom900_tmp = talib.MOM(raw_data['Close'], timeperiod=900)
# mom1800_tmp = talib.MOM(raw_data['Close'], timeperiod=1800)  # 1h
# mom5400_tmp = talib.MOM(raw_data['Close'], timeperiod=5400)  # 3h
# mom10800_tmp = talib.MOM(raw_data['Close'], timeperiod=10800)  # 6h
# mom21600_tmp = talib.MOM(raw_data['Close'], timeperiod=21600)  # 12h
# mom43200_tmp = talib.MOM(raw_data['Close'], timeperiod=43200)  # 1d
# mom129600_tmp = talib.MOM(raw_data['Close'], timeperiod=129600)  # 3d
# mom302400_tmp = talib.MOM(raw_data['Close'], timeperiod=302400)  # 7d
# mom1209600_tmp = talib.MOM(raw_data['Close'], timeperiod=1209600)  # 1M
raw_data['MOM5'] = mom5_tmp
raw_data['MOM15'] = mom15_tmp
raw_data['MOM100'] = mom100_tmp
raw_data['MOM300'] = mom300_tmp
# raw_data['MOM900'] = mom900_tmp
# raw_data['MOM1800'] = mom1800_tmp
# raw_data['MOM5400'] = mom5400_tmp
# raw_data['MOM10800'] = mom10800_tmp
# raw_data['MOM21600'] = mom21600_tmp
# raw_data['MOM43200'] = mom43200_tmp
# raw_data['MOM129600'] = mom129600_tmp
# raw_data['MOM302400'] = mom302400_tmp
# raw_data['MOM1209600'] = mom129600_tmp

raw_data.to_csv('out_test.csv', index=False)  # print(macd_tmp.tail())
