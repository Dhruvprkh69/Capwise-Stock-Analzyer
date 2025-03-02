from flask import Flask, render_template, request, redirect, url_for
import datetime
from fetch_stocks import fetch_cap_data

app = Flask(__name__)

# Cache data to avoid fetching on every request
data_cache = {
    "Large Cap": {"data": None, "timestamp": None},
    "Mid Cap": {"data": None, "timestamp": None},
    "Small Cap": {"data": None, "timestamp": None}
}

# Cache expiration time (1 hour)
CACHE_EXPIRY = 3600  # seconds

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stocks/<cap_type>')
def show_stocks(cap_type):
    if cap_type not in ["Large Cap", "Mid Cap", "Small Cap"]:
        return redirect(url_for('index'))
    
    current_time = datetime.datetime.now()
    cache_entry = data_cache[cap_type]
    
    # Check if cache is valid
    if (cache_entry["data"] is None or 
        cache_entry["timestamp"] is None or 
        (current_time - cache_entry["timestamp"]).total_seconds() > CACHE_EXPIRY):
        
        # Fetch fresh data
        stocks_df = fetch_cap_data(cap_type)
        
        if not stocks_df.empty:
            # Update cache
            data_cache[cap_type]["data"] = stocks_df.to_dict('records')
            data_cache[cap_type]["timestamp"] = current_time
        else:
            # Return empty list if no data
            data_cache[cap_type]["data"] = []
            data_cache[cap_type]["timestamp"] = current_time
    
    # Format update time
    if data_cache[cap_type]["timestamp"]:
        update_time = data_cache[cap_type]["timestamp"].strftime("%d-%b-%Y %I:%M %p")
    else:
        update_time = "Not available"
    
    return render_template(
        'stocks.html',
        cap_type=cap_type,
        stocks=data_cache[cap_type]["data"],
        update_time=update_time
    )

if __name__ == '__main__':
    app.run(debug=True)