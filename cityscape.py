import os
import pandas as pd
import calendar
import imgkit

# Constants
YEAR = 2023
MONTH = 9
TEMPLATE_PATH = 'templates/cityscape/template.html'
PARSED_TEMPLATE_PATH = 'templates/cityscape/parsed_template.html'
OUTPUT_DIR = 'output'
OUTPUT_FILE = 'output/cityscape.png'

def load_and_filter_data(csv_file, year, month):
    df = pd.read_csv(csv_file, encoding='ISO-8859-1')
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y %H:%M')
    return df[(df['Date'].dt.year == year) & (df['Date'].dt.month == month)]

def parse_template(template_path, data):
    with open(template_path, 'r') as file:
        template = file.read()
    for key, value in data.items():
        template = template.replace(f'{{{{ {key} }}}}', value)
    return template

def save_parsed_template(parsed_template, file_path):
    with open(file_path, 'w') as file:
        file.write(parsed_template)

def generate_image(input_file, output_file, options):
    if not os.path.exists(os.path.dirname(output_file)):
        os.makedirs(os.path.dirname(output_file))
    imgkit.from_file(input_file, output_file, options=options)

# Data processing
filtered_df = load_and_filter_data('data.csv', YEAR, MONTH)
collisions = len(filtered_df)

# Template parsing
data = {
    'year': str(YEAR),
    'month': calendar.month_name[MONTH],
    'collisions': str(collisions),
}
parsed_template = parse_template(TEMPLATE_PATH, data)
save_parsed_template(parsed_template, PARSED_TEMPLATE_PATH)

# Image generation
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
generate_image(PARSED_TEMPLATE_PATH, OUTPUT_FILE, options)

# Cleanup
if os.path.exists(PARSED_TEMPLATE_PATH):
    os.remove(PARSED_TEMPLATE_PATH)
