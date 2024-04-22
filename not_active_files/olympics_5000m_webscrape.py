# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:26:06 2024

@author: User
"""

from urllib import request, error
import re
from bs4 import BeautifulSoup

#soup = BeautifulSoup(html_source, 'html.parser')


def table_finder():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    req = request.Request(target, headers=headers)
    soup = BeautifulSoup(request.urlopen(req), 'html.parser')
    final_heading = soup.find('span', {'id': 'Final'})
    if final_heading:
        TAB = final_heading.find_next('table', class_='wikitable')
    else:
        final_classification_heading = soup.find('span', {'id': 'Final_classification'})
        TAB = final_classification_heading.find_next('table', class_='wikitable')
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
        file.write(','.join(column_headings) + '\n')
        
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
        
        
        
        #TAB = soup.find('table', class_="wikitable")
        if TAB:
            th_elements = TAB.find_all('th')
            column_headings = []
            
            # Extract the titles from the title attribute of the <button> elements inside the <th> elements
            for heading in th_elements:
                column_headings.append(heading.text.strip())
            if year == "2000":
                del column_headings[0]
            length_column_headings = len(column_headings)
            
            
            print("Table found")
        
        
            # Finding talbe row elements
            table_rows = TAB.find_all('tr')
            
            # Iterate through the rows to extract the data
            for row_index, row in enumerate(table_rows[1:], start=1):
                
                # Making a list of all the data elements from the row
                data_cells = row.find_all('td')
                
                if len(data_cells) >= length_column_headings:
                    
                    # Empty list to add the rows data to
                    row_contents = [year, location]
                    for cell_index, cell in enumerate(data_cells):
                    #print(cell)
                        cell_text = cell.text.strip()
                        
                        if cell_index == 0 and not cell_text:
                            span_element = cell.find('span', {'data-sort-value': True})
                            if span_element:
                                # Extract the value of the data-sort-value attribute
                                value = re.sub(r'^0', '', span_element['data-sort-value'].split()[0])
                                row_contents.append(value)

                            else:
                                row_contents.append(str(row_index))

                        else:
                            row_contents.extend([element.get_text(strip=True) for element in cell.contents if element.get_text(strip=True)])
                    
                    # adding notes column
                    if year == '2000':
                        del row_contents[5]   
                        
                    while len(row_contents) < 7:
                        row_contents.append('')
                        
                    if len(row_contents) > 7:
                        row_contents = row_contents[:7]
                    
                    if year == '1956':
                        del row_contents[-2]
                        row_contents.append('')

                    if row_contents[-1] not in ['DNF', 'PB', 'SB', 'NR', 'OR', 'WR']:
                        row_contents[-1] = ''
                else:
                    continue
                       
                if country_code_pattern.match(row_contents[4]):
                    country_code = country_code_pattern.match(row_contents[4]).group(1)
                    country_name = country_dict.get(country_code, row_contents[4])
                    row_contents[4] = country_name
                
                if row_contents[2].endswith('.'):
                    # Remove the full stop
                    row_contents[2] = row_contents[2][:-1]
                    
                if len(row_contents[5]) >= 6 and row_contents[5][5] == ':':
                    row_contents[5] = row_contents[5][:5] + '.' + row_contents[5][6:]
                    
                print(row_contents)
                        
                # Write the contents of the current row to the CSV file, joined by commas
                file.write(','.join(row_contents) + '\n')
        else:
            print("Table not found.")
            tables_not_found.append(year)
    
    
    except error.HTTPError as e:
        print("HTTP Error:", e)
    except error.URLError as e:
        print("URL Error:", e)

#1956 melbourne

years = ['1912', '1920', '1924', '1928', '1932', '1936', '1948', '1952', '1956', '1960', '1964', '1968', '1972', '1976', '1980', '1984', 
         '1988', '1992','1996', '2000', '2004', '2008', '2012', '2016', '2020']

locations = ['Stockholm', 'Antwerp', 'Paris', 'Amsterdam', 'Los Angeles', 'Berlin', 'London', 'Helsinki', 'Melbourne', 'Rome', 
             'Tokyo', 'Mexico City', 'Munich', 'Montreal', 'Moscow', 'Los Angeles', 'Seoul', 'Barcelona', 'Atlanta', 'Sydney', 
             'Athens', 'Beijing', 'London', 'Rio de Janeiro', 'Tokyo']

genders = ['Men', 'Women']

country_code_pattern = re.compile(r'^\((\w+)\)$') 

country_dict = {
    'AUS': 'Australia',
    'AUT': 'Austria',
    'BEL': 'Belgium',
    'BUL': 'Bulgaria',
    'CAN': 'Canada',
    'DEN': 'Denmark',
    'ESP': 'Spain',
    'ETH': 'Ethiopia',
    'EUA': 'United Team of Germany',
    'FIN': 'Finland',
    'FRA': 'France',
    'FRG': 'West Germany',
    'GBR': 'Great Britain',
    'GDR': 'East Germany',
    'GER': 'Germany',
    'HUN': 'Hungary',
    'IRL': 'Ireland',
    'ITA': 'Italy',
    'JPN': 'Japan',
    'KEN': 'Kenya',
    'MAR': 'Morocco',
    'NED': 'Netherlands',
    'NOR': 'Norway',
    'NZL': 'New Zealand',
    'POL': 'Poland',
    'POR': 'Portugal',
    'SUI': 'Switzerland',
    'SWE': 'Sweden',
    'TAN': 'Tanzania',
    'TCH': 'Czechoslovakia',
    'USA': 'United States',
    'URS': 'Soviet Union',
    'YUG': 'Yugoslavia'
}

for gender in genders:
    if gender == 'Women':
        years = years[-7:]
        locations = locations[-7:]
    with open(f'olympics_5000m_data_{gender.lower()}.csv', 'w', encoding='utf-8') as file:
        for index, year in enumerate(years):
            location = locations[index]
            tables_not_found = []
            #target = f'https://en.wikipedia.org/wiki/Athletics_at_the_{year}_Summer_Olympics_%E2%80%93_Men%27s_5000_metres'
            target = f'https://en.wikipedia.org/wiki/Athletics_at_the_{year}_Summer_Olympics_-_{gender}%27s_5000_metres'
            #extracting_titles()
            extracting_data()
            
countries_continents = [
    ['Algeria', 'Africa'],
    ['Australia', 'Oceania'],
    ['Austria', 'Europe'],
    ['Azerbaijan', 'Asia'],
    ['Bahrain', 'Asia'],
    ['Belgium', 'Europe'],
    ['Bulgaria', 'Europe'],
    ['Burundi', 'Africa'],
    ['Canada', 'North America'],
    ['China', 'Asia'],
    ['Czechoslovakia', 'Europe'],
    ['Denmark', 'Europe'],
    ['Djibouti', 'Africa'],
    ['East Germany', 'Europe'],
    ['Eritrea', 'Africa'],
    ['Ethiopia', 'Africa'],
    ['Finland', 'Europe'],
    ['FR Yugoslavia', 'Europe'],
    ['France', 'Europe'],
    ['Germany', 'Europe'],
    ['Great Britain', 'Europe'],
    ['Guatemala', 'North America'],
    ['Hungary', 'Europe'],
    ['Ireland', 'Europe'],
    ['Israel', 'Asia'],
    ['Italy', 'Europe'],
    ['Japan', 'Asia'],
    ['Kenya', 'Africa'],
    ['Latvia', 'Europe'],
    ['Mexico', 'North America'],
    ['Morocco', 'Africa'],
    ['Netherlands', 'Europe'],
    ['New Zealand', 'Oceania'],
    ['Norway', 'Europe'],
    ['Peru', 'South America'],
    ['Poland', 'Europe'],
    ['Portugal', 'Europe'],
    ['Qatar', 'Asia'],
    ['Romania', 'Europe'],
    ['Russia', 'Europe'],
    ['South Africa', 'Africa'],
    ['Soviet Union', 'Europe/Asia'],
    ['Spain', 'Europe'],
    ['Sweden', 'Europe'],
    ['Switzerland', 'Europe'],
    ['Tanzania', 'Africa'],
    ['Tunisia', 'Africa'],
    ['Turkey', 'Asia'],
    ['Uganda', 'Africa'],
    ['Ukraine', 'Europe'],
    ['United States', 'North America'],
    ['United Team of Germany', 'Europe'],
    ['West Germany', 'Europe']
]

with open('countries_and_continents.csv', 'w') as file:
    for country in countries_continents:
        # Write the contents of the current row to the CSV file, joined by commas
        file.write(','.join(country) + '\n')