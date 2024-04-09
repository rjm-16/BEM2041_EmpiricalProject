# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:06:17 2024

@author: User
"""

from bs4 import BeautifulSoup

# Sample HTML source code
html_source = """
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

# Extract data
table_rows = soup.find_all('tr')
print(table_rows)

for row in table_rows:
    data_cells = row.find_all('td')
    for cell in data_cells:
        print(cell.text, end='\t')
    print()  # Newline after each row