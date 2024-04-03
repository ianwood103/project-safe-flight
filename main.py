import os
import imgkit

def parse_template(template, data):
    for key, value in data.items():
        template = template.replace(f'{{{{ {key} }}}}', value)
    return template

options = {
    'format': 'png',
    'crop-h': '322',
    'crop-w': '208',
    'crop-x': '8',
    'crop-y': '8',
	'enable-local-file-access': None,
	'quality': '100'
}

data = {
    'collisions': '33',
    'month': 'February'
}

with open('templates/cityscape/template.html', 'r') as file:
    template = file.read()

parsed_template = parse_template(template, data)
    
with open('templates/cityscape/parsed_template.html', 'w') as file:
    file.write(parsed_template)

if not os.path.exists("output"):
    os.makedirs("output")
imgkit.from_file('templates/cityscape/parsed_template.html', 'output/cityscape.png', options=options)