import matplotlib.pyplot as plt
import pandas as pd
import imgkit
import os
import argparse

parser = argparse.ArgumentParser(description="Generator for city scape design.")
parser.add_argument("-year", "--year", type=int, required=True, help="Year")
parser.add_argument("-month", "--month", type=int, required=True, help="Month")
args = parser.parse_args()

# Constants
YEAR = args.year
MONTH = args.month

data = pd.read_csv('data.csv', encoding='ISO-8859-1')
data['Date'] = pd.to_datetime(data['Date'])
filtered_data = data[(data['Date'].dt.year == YEAR) & (data['Date'].dt.month == MONTH)]

value_counts = filtered_data['Species'].value_counts()
labels = value_counts.axes[0]
y = value_counts.array

plt.pie(y, labels=labels)
plt.savefig('templates/piechart/chart.png')

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

imgkit.from_file("templates/piechart/template.html", "output/piechart.png", options=options)

if os.path.exists("templates/piechart/chart.png"):
    os.remove("templates/piechart/chart.png")