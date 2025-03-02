#fetch_stocks.py
import datetime
import pandas as pd
from openchart import NSEData
from configs import STOCKS

def fetch_cap_data(cap_type):
    """Fetch stock data for Large, Mid, and Small cap stocks using OpenChart."""
    nse = NSEData()
    nse.download()
    stocks = STOCKS.get(cap_type, [])

    start_date = datetime.datetime.now() - datetime.timedelta(days=365)
    end_date = datetime.datetime.now()

    results = []
    for stock in stocks:
        try:
            data = nse.historical(
                symbol=stock.replace(".NS", ""),
                exchange="NSE",
                start=start_date,
                end=end_date,
                interval="1d"
            )
            
            if data is None or data.empty:
                print(f"Skipping {stock} (No Data Found)")
                continue
            
            data.columns = data.columns.str.lower()
            
            if not all(col in data.columns for col in ["high", "low", "close"]):
                print(f"Skipping {stock} (Missing required columns)")
                continue

            high_52_week = data["high"].max()
            low_52_week = data["low"].min()
            current_price = data["close"].iloc[-1]
            percent_down = ((high_52_week - current_price) / high_52_week) * 100

            results.append({
                "Company": stock,
                "Current Price": round(current_price, 2),
                "52-Week Low": round(low_52_week, 2),
                "52-Week High": round(high_52_week, 2),
                "% Down from High": round(percent_down, 2)
            })
        except Exception as e:
            print(f"Error fetching data for {stock}: {e}")

    return pd.DataFrame(results).sort_values(by="% Down from High", ascending=False)

if __name__ == "__main__":
    cap_type = "Large Cap"  # Change this for Mid/Small Cap
    df = fetch_cap_data(cap_type)
    if not df.empty:
        df.to_csv(f"{cap_type}_stocks.csv", index=False)
        print(df)
    else:
        print(f"No data available for {cap_type} stocks.")
