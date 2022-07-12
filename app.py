from dis import dis
import enum
from math import dist
from bs4 import BeautifulSoup
import pandas as pd
import requests

START_URL = (
    'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
)

browser = requests.get(START_URL)

soup = BeautifulSoup(browser.text, "html.parser")
temp_list = []

for tr in soup.find("table").find_all("tr"):
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

name = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])

df = pd.DataFrame(
    list(zip(name, distance, mass, radius)),
    columns=["Star_name", "Distance", "Mass", "Radius"],
)
df.to_csv("data.csv")

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(url)

soup = BeautifulSoup(browser.text, "html.parser")

start_table = soup.find_all('table')

table_rows = start_table[7].finad_all('tr')

for i in range(1, len(temp_list)):
    name.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

df2 = pd.DataFrame(list(zip(name, distance, mass, radius)),columns=['name','distance','mass','radius'])
print(df2)

df2.to_csv('dwarkStars.csv')