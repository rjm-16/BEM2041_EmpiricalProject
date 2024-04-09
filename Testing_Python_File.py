# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:06:17 2024

@author: User
"""

from bs4 import BeautifulSoup

# Sample HTML source code
with open('source_html_code.txt', 'r', encoding="utf-8") as file:
    html_source = file.read()


short_html_source = """
<tr>
    <th class="fiso-lab-table__row-heading">
        <span class="fiso-lab-table__row-heading-rank" title="Rank: 1">1</span>
        <span class="fiso-lab-table__row-heading-title">
            <span class="fiso-lab-table__row-heading-primary-data" title="Le Roux Roets">L. Roets</span>
            <span class="fiso-lab-table__row-heading-secondary-data" title="Sharks">(SHA)</span>
        </span>
    </th>
    <td class="fiso-lab-table__sorted-column">7</td>
    <td class="">0</td>
    <td class="">0</td>
    <td class="">0</td>
    <td class="">19</td>
    <td class="">16</td>
    <td class="">60</td>
    <td class="">2</td>
    <td class="">0</td>
    <td class="">0</td>
    <td class="">2</td>
    <td class="">2</td>
    <td class="">5</td>
    <td class="">2</td>
    <td class="">0</td>
    <td class="">0</td>
    <td class="">0</td>
    <td class="">0</td>
</tr>
"""


# Parse the HTML
soup = BeautifulSoup(html_source, 'html.parser')

# Extract column titles - th code?
# table_titles = soup.find_all('th')

# Extract data
TAB = soup.find('table', class_="fiso-lab-table")
table_rows = TAB.find_all('tr')
#print(table_rows)

for row in table_rows:
    name_span = row.find('span', class_='fiso-lab-table__row-heading-primary-data')
    team_span = row.find('span', class_='fiso-lab-table__row-heading-secondary-data')
        
    if name_span and team_span:
        name = name_span.get_text(strip=True)
        team = team_span.get_text(strip=True)
        print("Name:", name)
        print("Team:", team)
        print()
    
    data_cells = row.find_all('td')
    for cell in data_cells:
        print(cell.text, end='\t')
    print()  # Newline after each row
    
# table heading lines
th_elements = TAB.find('thead').find_all('th')

# Extract the titles from the title attribute of the <button> elements inside the <th> elements
column_titles = [th.find('button').get('title') for th in th_elements if th.find('button')]

# Add "Name" and "Club" at the start of the list
column_titles = ["Name", "Club"] + column_titles

# Print the column titles
print(column_titles)

with open('Super_Six_Data.csv', 'w') as file:
    file.write(','.join(column_titles))


    