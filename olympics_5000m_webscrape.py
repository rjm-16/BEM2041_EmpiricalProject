# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:26:06 2024

@author: User
"""

from urllib import request, error
import re
from bs4 import BeautifulSoup



with open('Olympic_source_code.txt', 'r', encoding="utf-8") as file:
    html_source = file.read()

#soup = BeautifulSoup(html_source, 'html.parser')


def table_finder():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    req = request.Request(target, headers=headers)
    soup = BeautifulSoup(request.urlopen(req), 'html.parser')
    final_heading = soup.find('span', {'id': 'Final'})
    TAB = final_heading.find_next('table', class_='wikitable')
    return TAB

#print(TAB)

def extracting_titles():
    try:
        # Send the request with the specified headers
        TAB = table_finder()
        #TAB = soup.find('table', class_='wikitable')
        if TAB:
            print("Table found")
        else:
            print("Table not found.")
    
        # table heading lines
        th_elements = TAB.find_all('th')
        
        column_headings = ['Year', 'Location']
        # Extract the titles from the title attribute of the <button> elements inside the <th> elements
        for heading in th_elements:
            column_headings.append(heading.text.strip())
        print(column_headings)
        
        # Write the column titles into the csv file joined by commas
        file.write(','.join(column_titles) + '\n')
        
    except error.HTTPError as e:
        print("HTTP Error:", e)
    except error.URLError as e:
        print("URL Error:", e)

def extracting_data():
    try:
        print(target)
        TAB = table_finder()
        #print(TAB)
        
        # table heading lines
        th_elements = TAB.find_all('th')
        column_headings = []
        # Extract the titles from the title attribute of the <button> elements inside the <th> elements
        for heading in th_elements:
            column_headings.append(heading.text.strip())
        
        
        #TAB = soup.find('table', class_="wikitable")
        if TAB:
            print("Table found")
        else:
            print("Table not found.")
        
        # Finding talbe row elements
        table_rows = TAB.find_all('tr')
            
        # Iterate through the rows to extract the data
        for row in table_rows:
            
            
            # Skips first tr element that contain the headers
            if row == table_rows[0]:
                continue

            
            # Making a list of all the data elements from the row
            data_cells = row.find_all('td')
            
            # Iterate through the data elements within the row to extract the data from the row, 
            # removing commas and leading/trailing whitespace then appending to the row_contents
            if len(data_cells) == len(column_headings):
                # Empty list to add the rows data to
                row_contents = [year, location]
                for cell in data_cells:
                #print(cell)
                
                    if cell == data_cells[0]:
                        if cell.text.strip() == '':
                            
                            if cell.contents:
                                span_element = cell.find('span', {'data-sort-value': True})
                                # Extract the value of the data-sort-value attribute
                                value = span_element['data-sort-value']
                                numeric_part = value.split()[0]
                                (row_contents.append(numeric_part[1]))
                            else:
                                row_contents.append(cell.text.strip())
                        else:
                            row_contents.append(cell.text.strip())
                    else:
                        separate_values = [element.get_text(strip=True) for element in cell.contents if element.get_text(strip=True)]
                        row_contents.extend(separate_values)
                # adding notes column
                while len(row_contents) < 7:
                    row_contents.append('')
            else:
                continue
                    
            print(row_contents)
                    
            # Write the contents of the current row to the CSV file, joined by commas
            file.write(','.join(row_contents) + '\n')    
    
    
    except error.HTTPError as e:
        print("HTTP Error:", e)
    except error.URLError as e:
        print("URL Error:", e)
        
years = ['1912', '1920', '1924', '1928']
locations = ['Stockholm', 'Antwerp', 'Paris', 'Amsterdam']
with open('olympics_5000m_data.csv', 'w', encoding='utf-8') as file:
    for index, year in enumerate(years):
        location = locations[index]
        target = f'https://en.wikipedia.org/wiki/Athletics_at_the_{year}_Summer_Olympics_%E2%80%93_Men%27s_5000_metres'
        #extracting_titles()
        extracting_data()

