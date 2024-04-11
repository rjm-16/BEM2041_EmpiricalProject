# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:20:48 2024

@author: User
"""

## Ladder Scrape

from urllib import request, error
from bs4 import BeautifulSoup
import re

with open('ladder_source_html_code.txt', 'r', encoding="utf-8") as file:
    html_source = file.read()
    
# Parse the HTML
soup = BeautifulSoup(html_source, 'html.parser')

TAB = soup.find('table', class_="fiso-widgets-ladder__table")
print(TAB)

table_rows = TAB.find_all('tr')

for row in table_rows:
        if row == table_rows[0]:
            continue
        
        # Empty list to add the rows data to
        row_contents = []

        # Making a list of all the data elements from the row
        data_cells = row.find_all('td')
        
        # Iterate through the data elements within the row to extract the data from the row, 
        # removing commas and leading/trailing whitespace then appending to the row_contents
        for cell in data_cells:
            if cell == data_cells[0] or cell == data_cells[2]:
                continue
            else:
                (row_contents.append(cell.text.strip()))
        
        print(row_contents)