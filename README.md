# Stock Analyzer - NSE Value Investing Tool

A Flask-based web application for analyzing stocks from the National Stock Exchange (NSE) of India. The app categorizes stocks into Large Cap, Mid Cap, and Small Cap, and helps identify potential value investment opportunities by showing which stocks are trading below their 52-week highs.

## Features

- **Stock Categories**: Browse stocks by market capitalization (Large Cap, Mid Cap, Small Cap)
- **Key Metrics**: View current price, 52-week high, 52-week low, and % down from high
- **Interactive UI**: Filter stocks, sort by different metrics, and print reports
- **Responsive Design**: Works on desktop and mobile devices
- **Data Caching**: Efficient data handling to minimize redundant API calls

## Usage

1. Run the application:
   ```
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. Select a market cap category (Large, Mid, or Small) to view stocks
4. Use the filter box to search for specific stocks
5. Review the percentage down from 52-week high to identify potential value opportunities

## Project Structure

```
flask-stock-app/
│── app.py                  # Main Flask application
│── config.py               # Stock list configuration 
│── fetch_stocks.py         # Functions to fetch and process stock data
│── templates/              # HTML templates
│   │── index.html          # Homepage with category selection
│   │── stocks.html         # Stock data display page
│── static/                 # Static assets
│   │── styles.css          # CSS styles
│── requirements.txt        # Project dependencies
│── README.md               # Project documentation
```

## Technical Details

- **Backend**: Python with Flask framework
- **Data Processing**: Pandas for data manipulation
- **Data Source**: NSE stock data via OpenChart library
- **Frontend**: HTML, CSS, JavaScript

## Customization

- Modify `configs.py` to add or remove stocks from each category
- Adjust cache expiry time in `app.py` to balance performance and data freshness
- Edit `styles.css` to customize the appearance

## Acknowledgements

- Data provided by National Stock Exchange (NSE) of India
- OpenChart library for simplified stock data access
- Icons from Font Awesome
