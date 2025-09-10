# StockVision-AI 📈  
*A Machine Learning–Powered Stock Market Analysis & Signal Generation Tool*  

StockVision-AI is a Python-based tool that fetches real-time intraday stock data, applies technical indicators, trains ML models, and generates buy/sell signals with confidence scores. It also includes a Monte Carlo simulation engine to analyze risk and return distributions.  

---

## 🚀 Features  
- **Live Market Data**: Fetches 15-minute interval intraday stock data (default: 60 days) using [yFinance](https://pypi.org/project/yfinance/).  
- **Technical Indicators**: Computes key indicators such as **MACD, RSI, Bollinger Bands, Momentum, Acceleration, Rate of Change (ROC), and Heikin-Ashi trends**.  
- **Machine Learning Pipeline**: Random Forest Classifier trained on engineered features to predict short-term trends.  
- **Signal Generation**: Combines ML predictions and indicator-based rules into actionable signals (*Strong Buy, Buy, Hold, Sell*) with confidence levels.  
- **Risk Simulation**: Monte Carlo simulation (1,000+ runs) models possible return distributions for portfolio risk assessment.  
- **Configurable**: Customize ticker, interval, and historical period from the command line.  

---

## 🛠️ Tech Stack  
- **Python 3**  
- **Libraries**: Pandas, NumPy, scikit-learn, yFinance, pytz  

---

## 📂 Project Structure  
```
stockvision-AI/
│── config.py          # Default settings (ticker, interval, timezone, etc.)
│── data_loader.py     # Fetches intraday stock data
│── indicators.py      # Computes MACD, RSI, Bollinger Bands, ROC, Momentum
│── heikin_ashi.py     # Generates Heikin-Ashi candlesticks & trend
│── ml_model.py        # Prepares features, trains Random Forest classifier
│── signal_generator.py# Combines ML + indicators to generate trading signals
│── simulation.py      # Monte Carlo simulations for risk analysis
│── run_analysis.py    # Orchestrates the full pipeline
│── main.py            # CLI entry point
│── requirements.txt   # Dependencies
```

---

## ▶️ Usage  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/sunday-pichai/stockvision-AI.git
   cd stockvision-AI
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the analysis**  
   ```bash
   python main.py
   ```

   You will be prompted for:  
   - Stock ticker (default: `RELIANCE.NS`)  
   - Interval (default: `15m`)  
   - Period (default: `60d`)  

4. **Example Output**  
   ```
   📈 RELIANCE.NS -> BUY (76.45% confidence)
   ```

---

## 📊 Example Workflow  
- Fetch intraday data from NSE/BSE stocks  
- Compute indicators + Heikin-Ashi candlesticks  
- Train ML model to predict next-interval movement  
- Generate actionable signals (BUY/SELL/HOLD)  
- Run Monte Carlo simulation to assess risks  

---

## 👨‍💻 Author  
**Kamalesh R**  
- [GitHub](https://github.com/sunday-pichai)  
