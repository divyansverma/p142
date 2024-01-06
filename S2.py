import requests
import pandas as pd
from bs4 import BeautifulSoup

dwarfstars_url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page=requests.get(dwarfstars_url)
#print(page)
soup =BeautifulSoup(page.text,"html.parser")
star_table=soup.find('table')
tem_list=[]
table_row=star_table.find_all('tr')
for row in table_row:
    td=row.find_all('td')
    r=[i.text.rstrip()for i in td]
    tem_list.append(r)
    
print(tem_list)
names=[]
distance=[]
mass=[]
radius=[]
for i in range(1,len(tem_list)):
    names.append(tem_list[i][0])
    distance.append(tem_list[i][5])
    mass.append(tem_list[i][8])
    radius.append(tem_list[i][9])
    

df=pd.DataFrame(list(zip(names,distance,mass,radius)),columns=["starnames","distance","mass","radius"])
print(df)
df.to_csv("dwarfstars.csv")  




















