--------------------------------------------------------------------------------
# BEM2041_EmpiricalProject
# Student ID: 710011110
--------------------------------------------------------------------------------
# Project README
## Date: 2024-04-25


## Introduction

This project is looking at the data on finishers of the marathon at the Olympic Games since 1896.
This project consists of a Python script for scraping data about the Olympic Marathon from Wikipedia, an SQL script for processing the scraped data, and a Jupyter Notebook for data analysis and creating visualisations. 
The output of the Jupyter Notebook is stored in a directories named '/figures' and '/tables'. 
Finally, the project is uploaded to a GitHub repository, and a HackMD file is used to embed the plots in a blog post.


## Contents

1. Python Scraping Script (`marathon_data_scrape.py`)
2. SQL Processing Script (`create_marathon_tables.sql`)
3. Jupyter Notebook (`marathon_data_analysis.ipynb`)
4. Figures Directory (`/figures`)
5. Tables Directory (`/tables`)
6. HackMD Blog Post (https://hackmd.io/@dQHzyA4YQAa_oNEvWkRADA/r1MpwKZlC)

## 1. Python Scraping Script (`marathon_data_scrape.py`)

The Python script scrapes data on the finishers of marathons at the Olympics from Wikipedia. It extracts data from Wikipedia pages for different years and genders, processes the data, and exports it as two CSV files (one for each gender). The script also creates a CSV file of all the countries and corresponding continents of each runners nationality.

## 2. SQL Processing Script (`create_marathon_tables.sql`)

The SQL script processes the scraped data using SQLite3. It creates tables for the individual genders data and countries_continents data, imports the CSV files generated by the scraping script, filters out the invalid data so all the remaining data is on finishers of the marathon with a recorded time, and combines the all data into a final combined table. It then exports the combined table as a CSV file (olympic_marathon_combined_data.csv) to be analysed in the Jupyter Notebook.

## 3. Jupyter Notebook (`marathon_data_analysis.ipynb`)

The Jupyter Notebook performs data analysis and creates visualisations of the data using pandas, matplotlib, numpy and datetime packages. It reads the olympic_marathon_combined_data.csv produced from the SQLite database to perform the analysis.

## 4. Figures Directory (`/figures`)

This directory contains the plots generated by the Jupyter Notebook. Which once pushed to GitHub have a direct link to the HackMD blog to automatically update.

## 5. Tables Directory (`/tables`)

This directory contains the tables generated by the Jupyter Notebook.

## 6. HackMD File (https://hackmd.io/@dQHzyA4YQAa_oNEvWkRADA/r1MpwKZlC)

Blog_Post_Markdown is the Markdown code behind the blog post created in HackMD. The HackMD file embeds the plots from the `/figures` directory into a blog post using permalinks from the GitHub repository https://github.com/rjm-16/BEM2041_EmpiricalProject


## Running Instructions
To run this project, ensure you have Python, SQLite, Jupyter Notebook, and the required Python packages (below) installed. Execute the Python scraping script first, followed by the SQL processing script. Finally, run the Jupyter Notebook for the data analysis.

This has been tested using Python 3.9.13

Python Packages along with the version number used to generate original results:
 > matplotlib 3.5.2
 > numpy 1.21.5
 > pandas 1.4.4

## About

This repository was generated by Rory Mitchell.
For queries: mailto:rjm251@exeter.ac.uk

