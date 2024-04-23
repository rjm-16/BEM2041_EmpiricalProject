# BEM2041_EmpiricalProject
# Student ID: 710011110

# Project README

This project consists of a Python script for scraping data from Wikipedia, an SQL script for processing the scraped data, and a Jupyter Notebook for data analysis and visualization. The output of the Jupyter Notebook is stored in a directory named '/figures'. Finally, the project is uploaded to a GitHub repository, and a HackMD file is used to embed the plots in a blog post.

## Contents

1. Python Scraping Script (`scraping.py`)
2. SQL Processing Script (`processing.sql`)
3. Jupyter Notebook (`analysis.ipynb`)
4. Figures Directory (`/figures`)
5. HackMD File (Blog Post)

## 1. Python Scraping Script (`scraping.py`)

The Python script scrapes data on the runners and finishers of marathons at the Olympics from Wikipedia. It extracts data from Wikipedia pages for different years and genders, processes the data, and exports it as CSV files.

## 2. SQL Processing Script (`processing.sql`)

The SQL script processes the scraped data using SQLite. It creates tables, imports CSV files generated by the scraping script, modifies the schema, filters invalid data, and combines the data from different sources into a final combined table.

## 3. Jupyter Notebook (`analysis.ipynb`)

The Jupyter Notebook performs data analysis and visualization using pandas, matplotlib, and numpy. It reads the combined data from the SQLite database, converts time strings to timedelta format, calculates time differences, and plots winning times from 1896 to 2020 for men and women.

## 4. Figures Directory (`/figures`)

This directory contains the figures generated by the Jupyter Notebook. The winning times plot is saved as `winning_times_plot.png`.

## 5. HackMD File (Blog Post)

The HackMD file embeds the plots from the `/figures` directory into a blog post using permalinks.

To run this project, ensure you have Python, SQLite, Jupyter Notebook, and the required Python packages installed. Execute the Python scraping script first, followed by the SQL processing script. Finally, run the Jupyter Notebook for data analysis and visualization.

```
