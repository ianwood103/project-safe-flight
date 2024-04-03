import pandas as pd
import folium
from selenium import webdriver
import time
import os

def create_map_for_month_year(csv_file, year, month):
    # Load the CSV file
    data = pd.read_csv(csv_file, encoding='ISO-8859-1')

    # Convert 'Date' column to datetime
    data['Date'] = pd.to_datetime(data['Date'])

    # Filter by the specified month and year
    filtered_data = data[(data['Date'].dt.year == year) & (data['Date'].dt.month == month)]

    # Starting location for the map
    if not filtered_data.empty:
        start_coords = (filtered_data.iloc[0]['y'], filtered_data.iloc[0]['x'])
    else:
        start_coords = (0, 0)  # Default location if no data is available

    my_map = folium.Map(location=start_coords, zoom_start=13)

    # Add a marker for each lat-long pair
    for index, row in filtered_data.iterrows():
        folium.Marker((row['y'], row['x']), popup=f'{row["Date"]}').add_to(my_map)

    # Save the map as an HTML file
    my_map.save('my_map.html')

    # Use selenium to open the map in a browser and take a screenshot
    driver = webdriver.Chrome()
    driver.get('file://' + os.path.realpath('my_map.html'))
    time.sleep(5)  # Wait for the map to load completely
    driver.save_screenshot('my_map.png')  # Save the screenshot as an image
    driver.quit()

    return 'Map saved as my_map.png'

# Example usage: create a map for April 2022
create_map_for_month_year('data.csv', 2023, 10)
