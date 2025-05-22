import ccxt
import pandas as pd
import logging

def fetch_ohlcv(symbol="ETH/USDT", timeframe="5m", limit=500):
    try:
        exchange = ccxt.binanceus({
            'enableRateLimit': True
        })

        logging.info(f"Fetching {symbol} data from Binance US...")
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)

        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

        return df

    except Exception as e:
        logging.error(f"Error fetching OHLCV data: {e}")
        raise
