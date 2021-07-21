from pycoingecko import CoinGeckoAPI
import pandas as pd
from datetime import date, timedelta
import time
import json

sdate = date(2012,1,1) # start date
edate = date(2021,7,12) # end date

sunixtime = time.mktime(sdate.timetuple())
eunixtime = time.mktime(edate.timetuple())

cg = CoinGeckoAPI()

crypto = 'bitcoin'

def get_prices(crpyto,s,e):
    price = cg.get_coin_market_chart_range_by_id(id=crpyto,from_timestamp=s,to_timestamp=e,vs_currency='usd')
    return pd.DataFrame.from_dict(price.get('prices'))

df = get_prices(crypto,sunixtime,eunixtime)

df.columns = ['dt','price']

df['dt'] = pd.to_datetime(df['dt'],unit='ms')

def write_data(df):
    print(f"Number of days printed: {len(df)}")
    print(f"Minimum Date found: {df.dt.min()}")
    print(f"Maximum Date found: {df.dt.max()}")
    df.to_csv('btc_prices.csv',index=False)

write_data(df)