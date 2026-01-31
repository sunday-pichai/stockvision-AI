import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler


def prepare_ml_data(df: pd.DataFrame):
    df = df.copy()

    # future return with noise filter
    df["future_return"] = df["Close"].pct_change().shift(-1)
    df["label"] = (df["future_return"] > 0.0005).astype(int)

    df = df.dropna()

    features = [
        "macd",
        "signal",
        "rsi",
        "boll_upper",
        "boll_lower",
    ]

    x = df[features]
    y = df["label"]

    return x, y, features


def train_ml(x, y):
    split = int(len(x) * 0.8)

    x_train = x.iloc[:split]
    x_test = x.iloc[split:]
    y_train = y.iloc[:split]
    y_test = y.iloc[split:]

    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=6,
        random_state=42,
        n_jobs=-1,
    )

    model.fit(x_train, y_train)
    accuracy = model.score(x_test, y_test)

    return model, scaler, accuracy
