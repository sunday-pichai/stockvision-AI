import numpy as np


def generate_signal(df, ha_df, model, scaler, features):
    if df.empty or ha_df.empty:
        return "no data", 0, 0.0

    latest = df.iloc[-1:]

    if latest[features].isnull().any().any():
        return "insufficient data", 0, 0.0

    x_latest = scaler.transform(latest[features])
    pred = model.predict(x_latest)[0]
    conf = float(np.max(model.predict_proba(x_latest)[0]))

    score = 0.0

    if pred == 1:
        score += 2.0 * conf
    else:
        score -= 2.0 * conf

    if df["macd"].iloc[-1] > df["signal"].iloc[-1]:
        score += 1.0

    if df["rsi"].iloc[-1] < 30:
        score += 1.0

    if ha_df["ha_trend"].iloc[-1] == 1:
        score += 1.0

    if score >= 3.5:
        decision = "strong buy"
    elif score >= 1.5:
        decision = "buy"
    elif score >= -1.0:
        decision = "hold"
    else:
        decision = "sell"

    return decision, pred, conf
