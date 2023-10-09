# -*- coding: utf-8 -*-
"""coding_assignment_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GgOvA8QxvHUEPw29-xm94E1izKHztaMY

Import the necessary libraries
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import scipy
from matplotlib import pyplot as plt

"""Request scraping from the website and initialize a BeautifulSoup object"""

opened_webpage = requests.get("https://en.wikipedia.org/wiki/List_of_cities_by_GDP")
bs = BeautifulSoup(opened_webpage.content, "html.parser")

"""Find all the tables on the website and add them as a string to a list. Since I am only concerned with the first table I extracted that table from the list of tables and stored it in a variable called table_1"""

raw_data = []

table = bs.find_all("table")
count = 0

for row in table[1]:
    line = row.text
    raw_data.append(line)

table_1 = raw_data[1]
print(table_1)

"""Split the string that contais all the data of table 1 on a double newline.
Create a new clean list that stores the data by removing extraneous newlines.
"""

#split string on double new line to get each cell as its own list item
df_list = table_1.split("\n\n")
#create a clean list with each cell with no newline characters
new_df_list = []
for data in df_list:
  clean_data = data.replace("\n","")
  new_df_list.append(clean_data)
new_df_list

"""Iterate through a list containing all data and add each row of data to a list, which will be appended to a list containing all rows"""

rows = []
counter = 0
current_row = []
for i in range(0, len(new_df_list)):
  counter +=1
  if counter < 6:
    current_row.append(new_df_list[i])
  else:
    current_row.append(new_df_list[i])
    rows.append(current_row)
    current_row = []
    counter = 0

"""Create a list of column names by extracting the first list from list of rows.
The rest of the lists in the list will be our body of data.
"""

column_names = rows[0]

data_body = rows[1:(len(rows)+1)]

"""Put our clean list of lists which contain data from each of the rows into a dataframe, passing in the column names to specify."""

raw_df = pd.DataFrame(data_body, columns = column_names)
raw_df

"""Checking for duplicate data"""

number_of_duplicates = raw_df.duplicated().sum()
print (f" Number of duplicates before : {number_of_duplicates}")

raw_df.info()

"""Remove rows with missing GDP data."""

clean_df = raw_df.drop(raw_df[raw_df['Official est. GDPup to date(billion US$)'] == ''].index)
clean_df

"""Write a function to convert numeric data into datatype float so that it may be used in analysis."""

def clean_and_convert(info):
  if "(" in info:
    list_1 = info.split("(")
    clean_info = list_1[0]
    clean_info = clean_info.replace(",", '')
    clean_info = clean_info.replace("+", '')
    clean_info = float(clean_info)
    return clean_info
  elif "[" in info:
    list_1 = info.split("[")
    clean_info = list_1[0]
    clean_info = clean_info.replace(",", '')
    clean_info = clean_info.replace("+", '')
    clean_info = float(clean_info)
    return clean_info
  else:
    clean_info = info.replace(",", '')
    clean_info = float(clean_info)
    return clean_info

"""Appl the clean and convert function to columns with numeric data of interest"""

clean_df["Official est. GDPup to date(billion US$)"] = clean_df["Official est. GDPup to date(billion US$)"].apply(clean_and_convert)
clean_df["Metropolitan population"] = clean_df["Metropolitan population"].apply(clean_and_convert)
clean_df["Official est. GDP per capita"] = clean_df["Official est. GDP per capita"].apply(clean_and_convert)

clean_df

"""Save the data frame as csv"""

clean_df.to_csv("GDP_by_metro_area.csv")

"""Describe and visualize columns of numeric data"""

clean_df["Official est. GDPup to date(billion US$)"].describe()

hist1 = clean_df["Official est. GDPup to date(billion US$)"].hist(bins = 15)

clean_df["Metropolitan population"].describe()

hist2 = clean_df["Metropolitan population"].hist(bins = 15)

clean_df["Official est. GDP per capita"].describe()

hist3 = clean_df["Official est. GDP per capita"].hist(bins = 15)

"""Calculate the correlation coefficient of Official GDP and Metropolitan population"""

from scipy.stats import pearsonr

p = pearsonr(clean_df["Official est. GDPup to date(billion US$)"], clean_df["Metropolitan population"])
print (p[0])

"""Visualize this coefficient with a scatterplot comparing GDP by Metropolitan area"""

gdp_column = clean_df["Official est. GDPup to date(billion US$)"]
population_column = clean_df["Metropolitan population"]

plt.scatter(gdp_column,population_column, s = 9)

plt.xlabel("Official estimated GDP (in billion US$)")
plt.ylabel("Metropolitan population")

plt.title("GDP by population of metropolitan center")

"""Sort the data frame by the official GDP in descending order"""

sorted_df = clean_df.sort_values(by = ['Official est. GDPup to date(billion US$)'], ascending = False)
sorted_df

"""Create a bar graph of the cities with the top 15 GDPs"""

top_15_gdp = sorted_df["Official est. GDPup to date(billion US$)"][0:15]
city_15 = sorted_df["City proper/metropolitan area"][0:15]

plt.bar(city_15, top_15_gdp, color ='pink', width = 0.4)
# Now add axis labels with units
plt.xlabel("City proper/metropolitan area ")
plt.ylabel("GDP")

# We can add a title too
plt.title("Top 15 Metropolitan Areas by GDP")

plt.xticks(rotation=90)