# Scraping example
# * Instead of Streaming Financial Data - Webscraping
import time
from datetime import datetime
from threading import Thread

import requests
from bokeh.layouts import column  # type: ignore[import-not-found]
from bokeh.models import (  # type: ignore[import-not-found]
    Button,
    ColumnDataSource,
    HoverTool,  # type: ignore[import-not-found]
)
from bokeh.plotting import curdoc, figure  # type: ignore[import-not-found]
from bs4 import BeautifulSoup

# Data source for Bokeh
source = ColumnDataSource(
    {
        "author": [],
        "quote": [],
        "tags": [],
        "timestamp": [],
        "x": [],  # For positioning
        "y": [],  # For positioning
    }
)


def scrape_quotes():
    """Scrape quotes from quotes.toscrape.com"""
    url = "http://quotes.toscrape.com"
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = []
        quote_elements = soup.find_all("div", class_="quote")

        for quote_elem in quote_elements:
            text = quote_elem.find("span", class_="text").text.strip()
            author = quote_elem.find("small", class_="author").text.strip()
            tags = [tag.text for tag in quote_elem.find_all("a", class_="tag")]

            quotes.append(
                {
                    "author": author,
                    "quote": text[:50] + "...",  # Truncate for display
                    "tags": ", ".join(tags),
                    "timestamp": datetime.now().strftime("%H:%M:%S"),
                }
            )

        return quotes
    except Exception as e:
        print(f"Scraping error: {e}")
        return []


def update_data():
    """Update data source with fresh scraped data"""
    while True:
        new_quotes = scrape_quotes()
        if new_quotes:
            # Prepare data for Bokeh source
            x_coords = list(range(len(new_quotes)))
            y_coords = [i % 10 for i in range(len(new_quotes))]

            new_data = {
                "author": [q["author"] for q in new_quotes],
                "quote": [q["quote"] for q in new_quotes],
                "tags": [q["tags"] for q in new_quotes],
                "timestamp": [q["timestamp"] for q in new_quotes],
                "x": x_coords,
                "y": y_coords,
            }

            # Update Bokeh source (thread-safe)
            source.stream(new_data, rollover=20)  # Keep last 20 quotes

        time.sleep(30)  # Update every 30 seconds


# Create Bokeh figure
p = figure(
    title="Live Web Scraping Dashboard",
    x_range=(0, 10),
    y_range=(0, 10),
    height=500,
    width=800,
    tools="pan,wheel_zoom,box_zoom,reset,save",
)

# Scatter plot colored by quote position
r = p.scatter(
    "x",
    "y",
    size=300,
    source=source,
    fill_color="navy",
    alpha=0.6,
    legend_label="Latest Quotes",
)

# Add hover with quote details
hover = HoverTool(
    tooltips=[
        ("Author", "@author"),
        ("Quote", "@quote"),
        ("Tags", "@tags"),
        ("Time", "@timestamp"),
    ]
)
p.add_tools(hover)

# Refresh button
refresh_btn = Button(label="Refresh Now", button_type="success")


def refresh_callback():
    new_quotes = scrape_quotes()
    if new_quotes:
        x_coords = list(range(len(new_quotes)))
        y_coords = [i % 10 for i in range(len(new_quotes))]
        new_data = {
            "author": [q["author"] for q in new_quotes],
            "quote": [q["quote"] for q in new_quotes],
            "tags": [q["tags"] for q in new_quotes],
            "timestamp": [q["timestamp"] for q in new_quotes],
            "x": x_coords,
            "y": y_coords,
        }
        source.stream(new_data, 5)  # Add up to 5 new points


refresh_btn.on_click(refresh_callback)

# Layout
layout = column(p, refresh_btn, width=800)

# Add to current document
curdoc().add_root(layout)
curdoc().title = "Live Scraper Dashboard"

# Start background scraping thread
scraping_thread = Thread(target=update_data, daemon=True)
scraping_thread.start()

# Initial data load
initial_quotes = scrape_quotes()
if initial_quotes:
    x_coords = list(range(len(initial_quotes)))
    y_coords = [i % 10 for i in range(len(initial_quotes))]
    source.data.update(
        {
            "author": [q["author"] for q in initial_quotes],
            "quote": [q["quote"] for q in initial_quotes],
            "tags": [q["tags"] for q in initial_quotes],
            "timestamp": [q["timestamp"] for q in initial_quotes],
            "x": x_coords,
            "y": y_coords,
        }
    )
