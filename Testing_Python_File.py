# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:06:17 2024

@author: User
"""

from urllib import request, error
from bs4 import BeautifulSoup
import re

# Sample HTML source code
with open('source_html_code.txt', 'r', encoding="utf-8") as file:
    html_source = file.read()


# Parse the HTML
soup = BeautifulSoup(html_source, 'html.parser')

# Extract table and split into rows of data
TAB = soup.find('table', class_="fiso-lab-table")
table_rows = TAB.find_all('tr')
    
# table heading lines
th_elements = TAB.find('thead').find_all('th')

# Extract the titles from the title attribute of the <button> elements inside the <th> elements
column_titles = [th.find('button').get('title') for th in th_elements if th.find('button')]

# Add "Name" and "Club" at the start of the list
column_titles = ["Name", "Club"] + column_titles

# Funcion to remove commas in the data so number >999 are interpeted as a single number using regular expressions
def remove_commas(text):
    return re.sub(r',','', text)

# Function to remove leading/trailing brackets
def strip_brackets(text):
    return re.sub(r'^\(|\)$', '', text)

# Create and open a csv file to write data into and assign it to the variable 'file'
with open('Super_Six_Data.csv', 'w') as file:
    
    # Write the column titles into the csv file joined by commas
    file.write(','.join(column_titles))
    
    # Iterate through the rows to extract the data
    for row in table_rows:
        print(row)
        
        # Empty list to add the rows data to
        row_contents = []
        
        # Retrieving the name and team elements as it is not in a data field
        name_span = row.find('span', class_='fiso-lab-table__row-heading-primary-data')
        team_span = row.find('span', class_='fiso-lab-table__row-heading-secondary-data')
        
        # If both name_span and team_span found extract the text from the span elements stripping leading/trailing whitespace
        if name_span and team_span:
            name = name_span.get_text(strip=True)
            team = strip_brackets(team_span.get_text(strip=True))
            # Append the name and club to the row_contents list to then be added to the csv file
            row_contents.append(name)
            row_contents.append(team)
            
        # For the first row which is the titles to ensure another column isn't added
        elif row.find('span', class_='fiso-lab-table__column-heading-text'):
            None
            
        # If name_span and team_span not found assign value of not found to 'name' and 'team'
        else:
            row_contents.append("Name not found")
            row_contents.append("Team not found")
        
        # Append the name and club to the row_contents list to then be added to the csv file
        #row_contents.append(name)
        #row_contents.append(team)
        
        # Making a list of all the data elements from the row
        data_cells = row.find_all('td')
        
        # Iterate through the data elements within the row to extract the data from the row, 
        # removing commas and leading/trailing whitespace then appending to the row_contents
        for cell in data_cells:
            (row_contents.append(remove_commas(cell.text.strip())))
            
        # Write the contents of the current row to the CSV file, joined by commas
        file.write(','.join(row_contents) + '\n')

    