# Coding-Assignment-1

The goal of this project was to analyze the GDP of metropolitan areas by population. It aimed to determine which areas had the top 15 GDPs, and if there was a correlation between population of a metropolitan area and the official estimated GDP.

Beautiful Soup was used to scrape the webpage I used, which has documentation that can be found here : https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Attributes fro this data set are:

Rank which which is the datatype string. Rank is a categorical variable that shows the relative ranking of GDP from highest to lowest among the metropolitan areas included in the dataset.

City/metropolitan area contains datatype string, which is a categorical descriptor of the metropolitan area the data was collected for.

Country/region area contains datatype string, which is a categorical descriptor of the country the metropolitan area is within.

The attribute Official est. GDPup to date (billion US$) is a variable of datatype float which contains numeric data of the official estimated GDP of the metropolitan area in question.

The attribute Metropolitan population is a variable of datatype float which contains numeric data of the population of each metropolitan area. 

The attribute Official GDP per capita is a variable of datatype float which contains numeric data of the official estimated GDP adjusted for population of the metropolitan area.

Potential issues with this dataset is that it came from Wikipedia, so has not been reviewed or collected by officials. It also had some missing data, which was removed for analysis but may have otherwise affected the data if it had been present. 
