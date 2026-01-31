import pandas as pd
import numpy as np


def heikin_ashi(df: pd.DataFrame) -> pd.DataFrame:
    required_cols = ["Open", "High", "Low", "Close"]
    if not all(col in df.columns for col in required_cols):
        raise ValueError("missing ohlc columns")

    ha = pd.DataFrame(index=df.index)

    ha["ha_close"] = (df["Open"] + df["High"] + df["Low"] + df["Close"]) / 4

    ha_open = np.empty(len(df))
    ha_open[0] = (df["Open"].iloc[0] + df["Close"].iloc[0]) / 2

    for i in range(1, len(df)):
        ha_open[i] = (ha_open[i - 1] + ha["ha_close"].iloc[i - 1]) / 2

    ha["ha_open"] = ha_open

    ha["ha_high"] = pd.concat(
        [df["High"], ha["ha_open"], ha["ha_close"]], axis=1
    ).max(axis=1)

    ha["ha_low"] = pd.concat(
        [df["Low"], ha["ha_open"], ha["ha_close"]], axis=1
    ).min(axis=1)

    ha["ha_trend"] = np.where(ha["ha_close"] > ha["ha_open"], 1, -1)

    return ha
