# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:06:02 2024

@author: User
"""

from urllib import request, error
import re
from bs4 import BeautifulSoup

target = 'https://www.foxsports.com.au/rugby/super-rugby/stats/players?'
#editiondata=none&fromakamai=true&pt=none&device=DESKTOP&wpa=BB44D82C3D7223D393F2AE47579FB5EA6791ABE4
#&pageNumber=2

# Define a User-Agent header
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def extracting_titles():
    try:
        # Send the request with the specified headers
        req = request.Request(target, headers=headers)
        soup = BeautifulSoup(request.urlopen(req), 'html.parser')
        TAB = soup.find('table', class_="fiso-lab-table")
        if TAB:
            print("TAB worked")
        else:
            print("Table not found.")
    
        # table heading lines
        th_elements = TAB.find('thead').find_all('th')
    
        # Extract the titles from the title attribute of the <button> elements inside the <th> elements
        column_titles = [th.find('button').get('title') for th in th_elements if th.find('button')]
    
        # Add "Name" and "Club" at the start of the list
        column_titles = ["Name", "Club"] + column_titles
        print(column_titles)
        
        # Write the column titles into the csv file joined by commas
        file.write(','.join(column_titles))
        
    except error.HTTPError as e:
        print("HTTP Error:", e)
    except error.URLError as e:
        print("URL Error:", e)
    

#&category=attack&pageNumber=2
categories = ['attack']
#['attack', 'defence', 'kicking']
for category in categories:
    print(category)
    with open(f'super_six_{category}_data.csv', 'w') as file:
        file.write(category +'\n')
        target = target+'&category='+category
        extracting_titles()
        
    for page in range(1,26):
        #end number needs to be 26
        print(target+'&pageNumber='+str(page))


def extracting_data:
    try:
        # Send the request with the specified headers
        req = request.Request(target, headers=headers)
        soup = BeautifulSoup(request.urlopen(req), 'html.parser')
        TAB = soup.find('table', class_="fiso-lab-table")
        if TAB:
            print("TAB worked")
        else:
            print("Table not found.")
    
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
    
        # Create and open a csv file to write data into and assign it to the variable 'file'
        with open('Super_Six_Data.csv', 'w') as file:
            
            # Write the column titles into the csv file joined by commas
            file.write(','.join(column_titles))
            
            # Iterate through the rows to extract the data
            for row in table_rows:
                
                # Empty list to add the rows data to
                row_contents = []
                
                # Retrieving the name and team elements as it is not in a data field
                name_span = row.find('span', class_='fiso-lab-table__row-heading-primary-data')
                team_span = row.find('span', class_='fiso-lab-table__row-heading-secondary-data')
                
                # If both name_span and team_span found extract the text from the span elements stripping leading/trailing whitespace
                if name_span and team_span:
                    name = name_span.get_text(strip=True)
                    team = team_span.get_text(strip=True)
                # If name_span and team_span not found assign value of not found to 'name' and 'team'
                else:
                    name = "Name not found"
                    team = "Team not found"
                
                # Append the name and club to the row_contents list to then be added to the csv file
                row_contents.append(name)
                row_contents.append(team)
                
                # Making a list of all the data elements from the row
                data_cells = row.find_all('td')
                
                # Iterate through the data elements within the row to extract the data from the row, 
                # removing commas and leading/trailing whitespace then appending to the row_contents
                for cell in data_cells:
                    (row_contents.append(remove_commas(cell.text.strip())))
                    
                # Write the contents of the current row to the CSV file, joined by commas
                file.write(','.join(row_contents) + '\n')
    
    
    except error.HTTPError as e:
        print("HTTP Error:", e)
    except error.URLError as e:
        print("URL Error:", e)
   
    #'wisbb_standardTable'