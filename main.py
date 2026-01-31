from run_analysis import run_analysis
from config import default_ticker, default_interval, default_period


def clean_input(value, default):
    value = value.strip()
    return value if value else default


if __name__ == "__main__":
    print("stockvision-ai")
    print("=" * 40)

    ticker = clean_input(
        input(f"ticker [{default_ticker}]: "),
        default_ticker,
    )

    interval = clean_input(
        input(f"interval [{default_interval}]: "),
        default_interval,
    )

    period = clean_input(
        input(f"period [{default_period}]: "),
        default_period,
    )

    run_analysis(ticker, interval, period)
