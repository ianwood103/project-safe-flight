import pandas as pd
import folium
from selenium import webdriver
import time
import os
import imgkit

def create_map_for_month_year(csv_file, year, month):
    # Load the CSV file
    data = pd.read_csv(csv_file, encoding='ISO-8859-1')

    # Convert 'Date' column to datetime
    data['Date'] = pd.to_datetime(data['Date'])

    # Filter by the specified month and year
    filtered_data = data[(data['Date'].dt.year == year) & (data['Date'].dt.month == month)]

    # Starting location for the map
    start_coords = (33.75873004, -84.39060179)

    my_map = folium.Map(location=start_coords, zoom_start=15)

    # Add a marker for each lat-long pair
    for index, row in filtered_data.iterrows():
        folium.Marker((row['y'], row['x']), popup=f'{row["Date"]}').add_to(my_map)

    # Save the map as an HTML file
    my_map.save('raw_map.html')

    # Use selenium to open the map in a browser and take a screenshot
    driver = webdriver.Chrome()
    driver.get('file://' + os.path.realpath('raw_map.html'))
    time.sleep(5)  # Wait for the map to load completely
    driver.save_screenshot('templates/map/images/raw_map.png')  # Save the screenshot as an image
    driver.quit()

# Example usage: create a map for April 2022
create_map_for_month_year('data.csv', 2022, 10)

options = {
    'format': 'png',
    'crop-h': '644',
    'crop-w': '416',
    'crop-x': '16',
    'crop-y': '16',
    'enable-local-file-access': None,
    'quality': '100',
    'zoom': 2
}

imgkit.from_file("templates/map/template.html", "output/map.png", options=options)

if os.path.exists("raw_map.html"):
    os.remove("raw_map.html")

if os.path.exists("templates/map/images/raw_map.png"):
    os.remove("templates/map/images/raw_map.png")
