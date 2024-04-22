# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:02:39 2024

@author: User
"""

### Python file to scrape the data on the runners and finishers of marathon at the Olympics from Wikipedia ###

# Importing necessary modules
from urllib import request, error
import re
from bs4 import BeautifulSoup

# Function to find the target table in the HTML page
def table_finder():
    
    # Adding user-agent headers to avoid being blocked
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    req = request.Request(target, headers=headers)
    
    # Creating soup of the website source code
    soup = BeautifulSoup(request.urlopen(req), 'html.parser')
    
    # Printing the target URL for debugging
    print(target)
    
    # List of possible table IDs
    table_ids = ['Results', 'Final_ranking', 'Final_rankings', 'Result']
    
    # Looping through possible table IDs to find the table
    for table_id in table_ids:
        heading = soup.find('span', {'id': table_id})
        if heading:
            return heading.find_next('table', class_='wikitable')
    
    # If no table found returning none
    return None

# Function to extract data from the table
def extracting_data():
    
    #Try so that if html or Url errors are caught and reported
    try:
        
        # Calling function to find the table
        TAB = table_finder()
        
        # Proceeding if the table is found
        if TAB:
            
            # Extracting column headings and adding to a list
            th_elements = TAB.find_all('th')
            column_headings = []
            for heading in th_elements:
                column_headings.append(heading.text.strip())
            
            # Caluclating number of column headings
            length_column_headings = len(column_headings)

            # Finding table row elements
            table_rows = TAB.find_all('tr')
            
            # Iterating through the rows to extract the data
            for row_index, row in enumerate(table_rows[1:], start=1):
                data_cells = row.find_all('td')
                
                # Adjusting column headings to catch case where there are more headings columns than rows of data
                # The first row of data always has the most columns of data so good to check the size of the table
                if row_index == 1 and len(data_cells) < length_column_headings:
                    column_headings = column_headings[:len(data_cells)]
                    length_column_headings = len(column_headings)
                    
                # Processing rows with enough data cells
                if len(data_cells) >= length_column_headings:
                    
                    # Initializing row contents list with year and location
                    row_contents = [year, location]
                    
                    # Iterating through the cells to extract the data
                    for cell_index, cell in enumerate(data_cells):
                        cell_text = cell.text.strip()
                        
                        # Handling special case where position is an image rather than a number so cannot extract position
                        if cell_index == 0 and not cell_text:
                            span_element = cell.find('span', {'data-sort-value': True})
                            if span_element:
                                
                               # Extract the value of the data-sort-value attribute 
                               # Using regular expressions drop a leading zero
                               value = re.sub(r'^0', '', span_element['data-sort-value'].split()[0])
                               row_contents.append(value)
                            
                            # If no span element add the row index as the positionI
                            else:
                                row_contents.append(str(row_index))
                                
                        # Extracting text from other data cell and adding to the row contents list
                        else:
                            row_contents.extend([element.get_text(strip=True) for element in cell.contents if element.get_text(strip=True)])

                    # Adding empty values to end of row contents to ensure fixed length of each line
                    if len(row_contents) < 7:
                        row_contents.extend([''] * (7 - len(row_contents)))
                    
                    # Checking if row contents is longer than desired length    
                    if len(row_contents) > 7:
                        
                        # If final column is 'Notes' column remove the penultimate column then restrict row length to 7 elements
                        if column_headings[-1] == 'Notes':
                            del row_contents[-2]
                            row_contents = row_contents[:7]
                        
                        # Otherwise shorten the row length to 7 elements
                        else:
                            row_contents = row_contents[:7]

                    # Checking if last column ('Notes') contains anything not contained in list and replacing it with blank cell
                    if row_contents[-1] not in ['DNF', 'PB', 'SB', 'NR', 'OR', 'WR']:
                        row_contents[-1] = ''
                        
                    # Checking if nationality column has nationality as an abbreviation of the country using regular expresions
                    # If true then replaces the abbreviation with the corresponding country from country_dict e.g. (FRA) -> France
                    if country_code_pattern.match(row_contents[4]):
                        country_code = country_code_pattern.match(row_contents[4]).group(1)
                        country_name = country_dict.get(country_code, row_contents[4])
                        row_contents[4] = country_name
                        
                    # Removing the trailing '.' at the end of the position cell to ensure that it can be change to an integer value
                    if row_contents[2].endswith('.'):
                        row_contents[2] = row_contents[2][:-1]
                    
                    # Writing the row contents to the csv file
                    file.write(','.join(row_contents) + '\n')
                    
        # Printing a message if the table is not found and adding the year to the tables_not_found list
        else:
            print("Table not found.")
            tables_not_found.append(year)
            
    # Handling and describing errors with accessing the websites
    except error.HTTPError as e:
        print("HTTP Error for {year} {gender}:", e)
    except error.URLError as e:
        print("URL Error for {year} {gender} :", e)

# Regular expression pattern for country codes used to identify when the nationality is as a country code instead of the full country name
country_code_pattern = re.compile(r'^\((\w+)\)$') 

# Dictionary mapping country codes to full country names
country_dict = {
    'ARG': 'Argentina',
    'ARU': 'Aruba',
    'AUS': 'Australia',
    'BEL': 'Belgium',
    'BLR': 'Belarus',
    'BOL': 'Bolivia',
    'BRA': 'Brazil',
    'CAN': 'Canada',
    'CHI': 'Chile',
    'CHN': 'China',
    'COL': 'Colombia',
    'CRC': 'Costa Rica',
    'DEN': 'Denmark',
    'ECU': 'Ecuador',
    'ESP': 'Spain',
    'EST': 'Estonia',
    'ETH': 'Ethiopia',
    'FIN': 'Finland',
    'FRA': 'France',
    'FRG': 'West Germany',
    'GBR': 'Great Britain',
    'GER': 'Germany',
    'GRE': 'Greece',
    'GUM': 'Guam',
    'HKG': 'Hong Kong',
    'HON': 'Honduras',
    'HUN': 'Hungary',
    'IRL': 'Ireland',
    'ISR': 'Israel',
    'ISV': 'Virgin Islands',
    'ITA': 'Italy',
    'JPN': 'Japan',
    'KEN': 'Kenya',
    'KGZ': 'Kyrgyzstan',
    'KOR': 'South Korea',
    'LAO': 'Laos',
    'LTU': 'Lithuania',
    'MEX': 'Mexico',
    'MLT': 'Malta',
    'MGL': 'Mongolia',
    'NAM': 'Namibia',
    'NED': 'Netherlands',
    'NEP': 'Nepal',
    'NGR': 'Nigeria',
    'NOR': 'Norway',
    'NZL': 'New Zealand',
    'PER': 'Peru',
    'POL': 'Poland',
    'POR': 'Portugal',
    'PRK': 'North Korea',
    'PUR': 'Puerto Rico',
    'ROU': 'Romania',
    'RSA': 'South Africa',
    'RUS': 'Russia',
    'SIN': 'Singapore',
    'SLO': 'Slovenia',
    'SUI': 'Switzerland',
    'SWE': 'Sweden',
    'TCH': 'Czechoslovakia',
    'TJK': 'Tajikistan',
    'TUR': 'Turkey',
    'UKR': 'Ukraine',
    'USA': 'United States',
    'EUN': 'Unified Team',
    'VIE': 'Vietnam',
    'YUG': 'Yugoslavia',
    'ZAI': 'Zaire'
}

# List of the years the marathon took place
years = ['1896', '1900', '1904', '1908','1912', '1920', '1924', '1928', '1932', '1936', '1948', '1952', '1956', '1960', '1964', '1968', '1972', '1976', '1980', '1984', 
         '1988', '1992', '1996', '2000', '2004', '2008', '2012', '2016', '2020']

# List of corresponding locations to the years above
locations = ['Athens', 'Paris', 'St. Louis', 'London', 'Stockholm', 'Antwerp', 'Paris', 'Amsterdam', 'Los Angeles', 'Berlin', 'London', 'Helsinki', 'Melbourne', 'Rome', 
             'Tokyo', 'Mexico City', 'Munich', 'Montreal', 'Moscow', 'Los Angeles', 'Seoul', 'Barcelona', 'Atlanta', 'Sydney',
             'Athens', 'Beijing', 'London', 'Rio de Janeiro', 'Tokyo']

# List of genders
genders = ['Men', 'Women']

# List to store years where tables are not found
tables_not_found = []

# Looping through genders to make the csv files
for gender in genders:
    
    # Shortening the years and locations list for the Women as they only started competing in the marathon from the 1984 Olympic Games in Los Angeles
    if gender == 'Women':
        years = years[-10:]
        locations = locations[-10:]
    
    # Creating and opening csv file to write the extracted data to
    with open(f'olympics_marathon_{gender.lower()}.csv', 'w', encoding='utf-8') as file:
        
        # Looping through years and retrieving the corresponding location
        for index, year in enumerate(years):
            location = locations[index]
            
            # Generating the target URL to scrape the data from
            target = f'https://en.wikipedia.org/wiki/Athletics_at_the_{year}_Summer_Olympics_-_{gender}%27s_marathon'
            
            # Running function to extract the data from the target website
            extracting_data()

# Printing years where tables are not found            
print('Tables not found:')            
print(tables_not_found)

# List of countries and corresponding continents
countries_continents = [
    ['Afghanistan', 'Asia'],
    ['Algeria', 'Africa'],
    ['American Samoa', 'Oceania'],
    ['Andorra', 'Europe'],
    ['Angola', 'Africa'],
    ['Argentina', 'South America'],
    ['Aruba', 'North America'],
    ['Australia', 'Oceania'],
    ['Austria', 'Europe'],
    ['Azerbaijan', 'Asia'],
    ['Bahrain', 'Asia'],
    ['Belarus', 'Europe'],
    ['Belgium', 'Europe'],
    ['Belize', 'North America'],
    ['Bermuda', 'North America'],
    ['Bohemia', 'Europe'],
    ['Bolivia', 'South America'],
    ['Bosnia and Herzegovina', 'Europe'],
    ['Botswana', 'Africa'],
    ['Brazil', 'South America'],
    ['Bulgaria', 'Europe'],
    ['Burma', 'Asia'],
    ['Burundi', 'Africa'],
    ['Cambodia', 'Asia'],
    ['Cameroon', 'Africa'],
    ['Canada', 'North America'],
    ['Cape Verde', 'Africa'],
    ['Cayman Islands', 'North America'],
    ['Central African Republic', 'Africa'],
    ['Ceylon', 'Asia'],
    ['Chile', 'South America'],
    ['China', 'Asia'],
    ['Chinese Taipei', 'Asia'],
    ['Colombia', 'South America'],
    ['Costa Rica', 'North America'],
    ['Croatia', 'Europe'],
    ['Cuba', 'North America'],
    ['Cyprus', 'Asia'],
    ['Czech Republic', 'Europe'],
    ['Czechoslovakia', 'Europe'],
    ['Democratic Republic of the Congo', 'Africa'],
    ['Denmark', 'Europe'],
    ['Djibouti', 'Africa'],
    ['East Germany', 'Europe'],
    ['East Timor', 'Asia'],
    ['Ecuador', 'South America'],
    ['Egypt', 'Africa'],
    ['El Salvador', 'North America'],
    ['Eritrea', 'Africa'],
    ['Estonia', 'Europe'],
    ['Ethiopia', 'Africa'],
    ['Federated States of Micronesia', 'Oceania'],
    ['Fiji', 'Oceania'],
    ['Finland', 'Europe'],
    ['FR Yugoslavia', 'Europe'],
    ['France', 'Europe'],
    ['Georgia', 'Europe'],
    ['Germany', 'Europe'],
    ['Great Britain', 'Europe'],
    ['Greece', 'Europe'],
    ['Greenland', 'North America'],
    ['Grenada', 'North America'],
    ['Guam', 'Oceania'],
    ['Guatemala', 'North America'],
    ['Guinea', 'Africa'],
    ['Guyana', 'South America'],
    ['Haiti', 'North America'],
    ['Honduras', 'North America'],
    ['Hong Kong', 'Asia'],
    ['Hungary', 'Europe'],
    ['Iceland', 'Europe'],
    ['Independent Olympic Athletes', 'Other'],
    ['India', 'Asia'],
    ['Individual Olympic Athletes', 'Other'],
    ['Indonesia', 'Asia'],
    ['Iran', 'Asia'],
    ['Iraq', 'Asia'],
    ['Ireland', 'Europe'],
    ['Israel', 'Asia'],
    ['Italy', 'Europe'],
    ['Ivory Coast', 'Africa'],
    ['Jamaica', 'North America'],
    ['Japan', 'Asia'],
    ['Jordan', 'Asia'],
    ['Kazakhstan', 'Asia'],
    ['Kenya', 'Africa'],
    ['Kiribati', 'Oceania'],
    ['Kuwait', 'Asia'],
    ['Kyrgyzstan', 'Asia'],
    ['Laos', 'Asia'],
    ['Latvia', 'Europe'],
    ['Lebanon', 'Asia'],
    ['Lesotho', 'Africa'],
    ['Liberia', 'Africa'],
    ['Libya', 'Africa'],
    ['Liechtenstein', 'Europe'],
    ['Lithuania', 'Europe'],
    ['Luxembourg', 'Europe'],
    ['Macau', 'Asia'],
    ['Madagascar', 'Africa'],
    ['Malawi', 'Africa'],
    ['Malaysia', 'Asia'],
    ['Maldives', 'Asia'],
    ['Mali', 'Africa'],
    ['Malta', 'Europe'],
    ['Marshall Islands', 'Oceania'],
    ['Mauritania', 'Africa'],
    ['Mauritius', 'Africa'],
    ['Mexico', 'North America'],
    ['Moldova', 'Europe'],
    ['Monaco', 'Europe'],
    ['Mongolia', 'Asia'],
    ['Montenegro', 'Europe'],
    ['Morocco', 'Africa'],
    ['Mozambique', 'Africa'],
    ['Myanmar', 'Asia'],
    ['Namibia', 'Africa'],
    ['Nauru', 'Oceania'],
    ['Nepal', 'Asia'],
    ['Netherlands', 'Europe'],
    ['New Caledonia', 'Oceania'],
    ['New Zealand', 'Oceania'],
    ['Nicaragua', 'North America'],
    ['Niger', 'Africa'],
    ['Nigeria', 'Africa'],
    ['North Korea', 'Asia'],
    ['North Macedonia', 'Europe'],
    ['Northern Mariana Islands', 'Oceania'],
    ['Northern Rhodesia', 'Africa'],
    ['Norway', 'Europe'],
    ['Oman', 'Asia'],
    ['Pakistan', 'Asia'],
    ['Palau', 'Oceania'],
    ['Palestine', 'Asia'],
    ['Panama', 'North America'],
    ['Papua New Guinea', 'Oceania'],
    ['Paraguay', 'South America'],
    ['Peru', 'South America'],
    ['Philippines', 'Asia'],
    ['Poland', 'Europe'],
    ['Portugal', 'Europe'],
    ['Puerto Rico', 'North America'],
    ['Qatar', 'Asia'],
    ['Refugee Olympic Team', 'Other'],
    ['Republic of China', 'Asia'],
    ['Republic of the Congo', 'Africa'],
    ['Rhodesia', 'Africa'],
    ['Romania', 'Europe'],
    ['Russia', 'Europe'],
    ['Rwanda', 'Africa'],
    ['Saint Kitts and Nevis', 'North America'],
    ['Saint Lucia', 'North America'],
    ['Saint Vincent and the Grenadines', 'North America'],
    ['Samoa', 'Oceania'],
    ['San Marino', 'Europe'],
    ['Sao Tome and Principe', 'Africa'],
    ['Saudi Arabia', 'Asia'],
    ['Senegal', 'Africa'],
    ['Serbia', 'Europe'],
    ['Serbia and Montenegro', 'Europe'],
    ['Seychelles', 'Africa'],
    ['Sierra Leone', 'Africa'],
    ['Singapore', 'Asia'],
    ['Slovakia', 'Europe'],
    ['Slovenia', 'Europe'],
    ['Solomon Islands', 'Oceania'],
    ['Somalia', 'Africa'],
    ['South Africa', 'Africa'],
    ['South Korea', 'Asia'],
    ['South Sudan', 'Africa'],
    ['Soviet Union', 'Europe'],
    ['Spain', 'Europe'],
    ['Sri Lanka', 'Asia'],
    ['Sudan', 'Africa'],
    ['Suriname', 'South America'],
    ['Swaziland', 'Africa'],
    ['Sweden', 'Europe'],
    ['Switzerland', 'Europe'],
    ['Syria', 'Asia'],
    ['Tajikistan', 'Asia'],
    ['Tanzania', 'Africa'],
    ['Thailand', 'Asia'],
    ['Togo', 'Africa'],
    ['Tonga', 'Oceania'],
    ['Trinidad and Tobago', 'North America'],
    ['Tunisia', 'Africa'],
    ['Turkey', 'Asia'],
    ['Turkmenistan', 'Asia'],
    ['Tuvalu', 'Oceania'],
    ['Uganda', 'Africa'],
    ['Ukraine', 'Europe'],
    ['United Arab Emirates', 'Asia'],
    ['United States', 'North America'],
    ['Unified Team', 'Other'],
    ['United Team', 'Other'],
    ['United Team of Germany', 'Europe'],
    ['Uruguay', 'South America'],
    ['Uzbekistan', 'Asia'],
    ['Vanuatu', 'Oceania'],
    ['Vatican City', 'Europe'],
    ['Venezuela', 'South America'],
    ['Vietnam', 'Asia'],
    ['Virgin Islands', 'North America'],
    ['West Germany', 'Europe'],
    ['Yemen', 'Asia'],
    ['Yugoslavia', 'Europe'],
    ['Zaire', 'Africa'],
    ['Zambia', 'Africa'],
    ['Zimbabwe', 'Africa']
]

# Creating and opening csv file to write countries and corresponding continents to
with open('countries_and_continents_final_version.csv', 'w') as file:
    for country in countries_continents:
        file.write(','.join(country) + '\n')