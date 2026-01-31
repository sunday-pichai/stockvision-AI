import pandas as pd
import numpy as np


def compute_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["momentum"] = df["Close"].diff(3)
    df["acceleration"] = df["momentum"].diff(3)

    df["roc"] = df["Close"].pct_change(8) * 100

    fast = df["Close"].ewm(span=8, adjust=False).mean()
    slow = df["Close"].ewm(span=20, adjust=False).mean()
    df["macd"] = fast - slow
    df["signal"] = df["macd"].ewm(span=6, adjust=False).mean()

    window = 15
    mean = df["Close"].rolling(window).mean()
    std = df["Close"].rolling(window).std()

    df["boll_upper"] = mean + 1.5 * std
    df["boll_lower"] = mean - 1.5 * std

    delta = df["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(10).mean()
    avg_loss = loss.rolling(10).mean()

    rs = avg_gain / avg_loss.replace(0, np.nan)
    df["rsi"] = 100 - (100 / (1 + rs))

    return df.dropna()
