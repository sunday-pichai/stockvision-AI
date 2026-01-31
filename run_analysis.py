from data_loader import load_intraday_data
from indicators import compute_indicators
from heikin_ashi import heikin_ashi
from ml_model import prepare_ml_data, train_ml
from signal_generator import generate_signal
from simulation import monte_carlo_simulation


def run_analysis(ticker, interval, period):
    print(f"\nrunning analysis for {ticker}")
    print("-" * 40)

    df, msg = load_intraday_data(ticker, interval, period)
    if df.empty:
        print("data load failed:", msg)
        return

    print("data loaded:", msg)

    raw_df = df.copy()

    df = compute_indicators(df)
    if df.empty:
        print("indicator computation failed")
        return

    print("indicators computed")

    ha_df = heikin_ashi(raw_df)
    print("heikin ashi computed")

    x, y, features = prepare_ml_data(df)
    if x.empty:
        print("ml data preparation failed")
        return

    model, scaler, accuracy = train_ml(x, y)
    print(f"model trained | accuracy: {accuracy:.2%}")

    decision, pred, conf = generate_signal(df, ha_df, model, scaler, features)
    print(f"signal: {decision} | confidence: {conf:.2%}")

    mean_ret, std_ret, status = monte_carlo_simulation(df)
    if status == "Success":
        print(f"monte carlo mean: {mean_ret:.2f}% | std: {std_ret:.2f}%")
    else:
        print("monte carlo skipped:", status)

    print("-" * 40)
