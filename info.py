from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd 
import numpy as n
from random import random 
def data_Downloader():
    source = requests.get("https://www.worldometers.info/coronavirus/country/us/").text
    soup = BeautifulSoup(source,"lxml")

    table = soup.find("table", id = "usa_table_countries_today")
    table_data = table.tbody.find_all("tr")


    dict = {}
    for value in range(len(table_data )):
        try:
            key = (table_data[value].find_all("a", href = True)[0].string)
        except: 
            key = (table_data[value].find_all("td")[0].string)
        
        values = [j.string for j in table_data[value].find_all("td")]


        dict[key] = values


    column_names = ["Total Cases", "New Cases", "Total Deaths", "New Deaths", "Total Recovered", "Active", "Tot Cases/1M pop", "Tot Death 1/M pop"]

    df = pd.DataFrame(dict).iloc[1:,:].T.iloc[:,:8]
    df.index_name = "state"
    df.columns = column_names

    print(df.head())

    df.to_csv("live_data.csv")
    print("code worked")

data_Downloader()




