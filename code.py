from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import csv
import requests

START_URL =  "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars";
page = requests.get(START_URL)
print(page)

def scrape():

    soup = BeautifulSoup(page.text,"html.parser")

    starTable = soup.find('table');

    table_row = starTable.find_all('tr')
    temp_list = []

    for tr_tag in table_row:
        td_tags = tr_tag.find_all('td')

        row = [i.text.rstrip() for i in td_tags]
        temp_list.append(row)

    name =[];
    distance=[];
    mass =[];
    radius =[];

    for i in range(1,len(temp_list)):
        name.append(temp_list[1])
        distance.append(temp_list[3])
        mass.append(temp_list[5])
        radius.append(temp_list[6])

    df2 = pd.DataFrame(list(zip(name,distance,mass,radius)),columns=['Star_name','Distance','Mass','Radius'])
    

    df2.to_csv('bright_stars.csv')


scrape();
