import requests
from bs4 import BeautifulSoup
import json

# Define the URL to scrape
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

# Make a GET request to the URL and get the response
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element that contains the data we want to scrape
table = soup.find('table', class_='tablepress')

# Extract the table headers
headers = [header.text.strip() for header in table.find_all('th')]

# Extract the table rows
rows = []
for row in table.find_all('tr'):
    cells = [cell.text.strip() for cell in row.find_all('td')]
    if cells:
        rows.append(cells)

# Convert the table data to a list of dictionaries
data = []
for row in rows:
    data.append(dict(zip(headers, row)))

# Write the data to a JSON file
with open('bu_data.json', 'w') as outfile:
    json.dump(data, outfile)
