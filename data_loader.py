import yfinance as yf
import pandas as pd
from datetime import datetime, time
import pytz

from config import (
    timezone,
    market_open,
    market_close,
    valid_intervals,
    valid_periods,
)

def is_market_open():
    now_dt = datetime.now(pytz.timezone(timezone))
    now_time = now_dt.time()

    open_time = time(*market_open)
    close_time = time(*market_close)

    return now_dt.weekday() < 5 and open_time <= now_time <= close_time

def load_intraday_data(ticker, interval, period):
    if interval not in valid_intervals:
        return pd.DataFrame(), f"invalid interval: {interval}"

    if period not in valid_periods:
        return pd.DataFrame(), f"invalid period: {period}"

    market_status = "open" if is_market_open() else "closed"

    data = yf.download(
        ticker,
        interval=interval,
        period=period,
        progress=False,
        auto_adjust=False,
    )

    if data.empty:
        return pd.DataFrame(), f"no data returned for {ticker}"

    # flatten yfinance multiindex columns
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    required_cols = ["Open", "High", "Low", "Close", "Volume"]

    if not all(col in data.columns for col in required_cols):
        return pd.DataFrame(), f"incomplete ohlcv data: {list(data.columns)}"

    data = data[required_cols].dropna()

    if len(data) < 120:
        return pd.DataFrame(), "insufficient data (minimum 120 candles required)"

    return data, f"data loaded successfully. market is {market_status}."
