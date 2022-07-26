from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import pandas as pd

start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("./chromedriverc")
browser.get(start_url)

import time
time.sleep(10)

def scraper():
    headers = ["Star Name", "Distance", "Mass", "Radius"]
    star_data = []

    soup= BeautifulSoup(browser.page_source, "html.parser")
    star_table = soup.find('table')
    table_rows=star_table[7].find_all("tr")

    for ul_tag in soup.find_all("tr"): 
        td_tags= ul_tag.find_all("td")
        list1 = []
            
        for j in td_tags:
            list1.append(j.text.rstrip())
        

    star_data.append(list1)
    
    
    with open("mainn.csv","w") as file:
        writer= csv.writer(file)
        writer.writerow(headers)
        writer.writerows(star_data)
    
scraper()

df= pd.DataFrame(list(list1), columns= ["Star Name", "Distance","Mass", "Radius"])
df.to_csv("mainn.csv")
