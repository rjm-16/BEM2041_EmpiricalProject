# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:20:48 2024

@author: User
"""
## Ladder Scrape

from urllib import request, error
from bs4 import BeautifulSoup

target = 'https://www.foxsports.com.au/rugby/super-rugby/ladder'
    
# Define a User-Agent header
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
req = request.Request(target, headers=headers)
soup = BeautifulSoup(request.urlopen(req), 'html.parser')

TAB = soup.find('table', class_="fiso-widgets-ladder__table")
table_rows = TAB.find_all('tr')

with open('super_rugby_ladder.csv', 'w') as file:
    for row in table_rows:
        
        # Empty list to add the rows data to
        row_contents = []        
        
        if row == table_rows[0]:
            heading_cells = row.find_all('th')
            for cell in heading_cells:
                if cell == heading_cells[0] or cell == heading_cells[2]:
                    continue
                else:
                    (row_contents.append(cell.text.strip()))
        else:
            
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
        file.write(','.join(row_contents) + '\n')
