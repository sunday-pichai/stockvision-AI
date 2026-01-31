import numpy as np
import pandas as pd


def monte_carlo_simulation(
    df: pd.DataFrame,
    runs: int = 1000,
    window: int = 20,
    seed: int = 42,
):
    if "Close" not in df.columns:
        return 0.0, 0.0, "missing close column"

    returns = df["Close"].pct_change().dropna()

    if len(returns) < window:
        return 0.0, 0.0, "insufficient data"

    rng = np.random.default_rng(seed)

    results = []
    for _ in range(runs):
        sample = rng.choice(returns.values, size=window, replace=True)
        results.append((np.prod(1 + sample) - 1) * 100)

    mean_return = float(np.mean(results))
    std_return = float(np.std(results))

    return mean_return, std_return, "Success"
