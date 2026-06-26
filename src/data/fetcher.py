import pandas as pd 
import yfinance as yf 
 
def get_price_data(ticker, start_date, end_date): 
    try: 
        df = yf.download(ticker, start=start_date, end=end_date, progress=False) 
        if df.empty: return [] 
        df = df.reset_index() 
        df['time'] = pd.to_datetime(df['Date']) 
        df.set_index('time', inplace=True) 
        df.rename(columns={'Open':'open','High':'high','Low':'low','Close':'close','Volume':'volume'}, inplace=True) 
        return df[['open','high','low','close','volume']] 
    except Exception as e: 
        print(f"Error: {e}") 
        return [] 
 
def detect_market(ticker): 
    return "gold" if "GC" in ticker.upper() else "us_stock" 
 
def prices_to_df(prices): 
    if isinstance(prices, list): 
        if len(prices) == 0: return pd.DataFrame() 
        df = pd.DataFrame(prices) 
        if 'time' in df.columns: df['time'] = pd.to_datetime(df['time']); df.set_index('time', inplace=True) 
        return df 
    return prices 
 
def get_cache(): 
    return {} 
