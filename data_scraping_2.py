from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

starturl = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(starturl)

soup=BeautifulSoup(page.text,"html.parser")

star_table = soup.find_all('table')
table_rows = star_table [7].find_all('tr')

temp_list = []
for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)
    
star_names = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    star_names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])
    
df2 = pd.DataFrame(list(zip(star_names, distance, mass, radius )), columns = ['Star_name', 'Distance','Mass','Radius' ])
print(df2)

df2.to_csv("dwarf_stars.csv")