# Q1.Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
 
import requests
from bs4 import BeautifulSoup
import json

url = 'http://www.bu.edu/president/boston-university-facts-stats/'

# Make a request to the website and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table containing the data

table = soup.find('table')

# Find the table headers and rows
headers = table.find_all('th')
rows = table.find_all('tr')[1:]

# Initialize a list to store the data
data = []

# Loop over the rows and extract the data
for row in rows:
    values = [td.text.strip() for td in row.find_all('td')]
    data.append(dict(zip([header.text.strip() for header in headers], values)))

# Write the data to a JSON file
with open('bu_facts_stats.json', 'w') as f:
    json.dump(data, f, indent=4)


#Q2. Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file

url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Make a GET request to the URL and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table containing the data
table = soup.find('table')

# Find the table headers and rows
headers = [header.text.strip() for header in table.find_all('th')]
rows = table.find_all('tr')[1:]

# Initialize a list to store the data
data = []

# Loop over the rows and extract the data
for row in rows:
    values = [td.text.strip() for td in row.find_all('td')]
    data.append(dict(zip(headers, values)))

# Write the data to a JSON file
with open('uci_datasets.json', 'w') as f:
    json.dump(data, f, indent=4)

#Q3. Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

# Make a GET request to the URL and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table containing the data
table = soup.find_all('table')[1]

# Find the table headers and rows
headers = [th.text.strip() for th in table.find_all('th')]
rows = table.find_all('tr')[1:]

# Initialize a list to store the data
data = []

# Loop over the rows and extract the data
for row in rows:
    values = []
    for td in row.find_all('td'):
        if td.find('a'):
            value = td.find('a').text.strip()
        else:
            value = td.text.strip()
        values.append(value)
    if values:
        data.append(dict(zip(headers, values)))
# Write the data to a JSON file
with open('presidents.json', 'w') as f:
    json.dump(data, f, indent=4)
