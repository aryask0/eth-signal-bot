import pandas as pd

def generate_signal(df: pd.DataFrame) -> str:
    latest = df.iloc[-1]

    rsi = latest['rsi']
    macd = latest['macd']
    macd_signal = latest['macd_signal']

    if rsi < 30 and macd > macd_signal:
        return "BUY"
    elif rsi > 70 and macd < macd_signal:
        return "SELL"
    else:
        return "HOLD"
