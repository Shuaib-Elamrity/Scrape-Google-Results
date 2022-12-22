#!/usr/bin/env python
# coding: utf-8

# In[123]:
Location = input("Please Enter The City : ")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from selenium.webdriver.chrome.options import Options
from time import sleep
from parsel import Selector
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
options = Options()
#options.add_argument("--headless")
from datetime import date

driver = webdriver.Chrome(options=options)
driver.maximize_window()


location = Location.replace(' ','%20')

driver.get('https://www.google.com/localservices/prolist?g2lbs=AL1YbfU737UbBRHEQEDkntiZM8Nt8RfLAXuYIb5yhiksEj0okhm5Pev0nHZX9NoFpOFg-ICZqc3-Z_oGelwapjTHBnoEWd0W7fuIdIzI1PeJ5YTPCKt_kB8Y1uichea6zwIT4ZhzlPdB&hl=en-US&gl=us&cs=1&ssta=1&oq=general%20contractors%20{}&src=2&origin=https%3A%2F%2Fwww.google.com&serdesk=1&sa=X&q=general%20contractors%20{}&ved=0CAUQjdcJahcKEwjwypHFwo38AhUAAAAAHQAAAAAQDw&scp=ChdnY2lkOmdlbmVyYWxfY29udHJhY3RvchIAGgAqEkdlbmVyYWwgY29udHJhY3Rvcg%3D%3D&slp=MgCIAQBSBAgCIABAAQ%3D%3D'.format(location , location))
#search = driver.find_element(By.XPATH , '//input[@type="search"]')
#search.clear()
#search.send_keys("general contractors {}".format(location))



sleep(2)

data=[]    
def get_data():
    
    try:
        element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@role="list"]/div[@jscontroller="xkZ6Lb"]')))
    except:
        sleep(5)
        pass
    
    links = driver.find_elements(By.XPATH , '//div[@role="list"]/div[@jscontroller="xkZ6Lb"]')
    for x in links :
        
        try:
            Business_Name= x.find_element(By.XPATH , './/div[@class="NwqBmc"]/div').text
        except:
            Business_Name = '-'


        try:
            Rating = x.find_element(By.XPATH , './/div[@class="OJbIQb"]/div').text
        except:
            Rating = '-'

        try:
            No_of_Reviews = x.find_element(By.XPATH , './/div[contains(@aria-label,"reviews")]').text
        except:
            No_of_Reviews = '-'

        #scroll_down()

        try:
            Phone = x.find_element(By.XPATH , './/a[@aria-label="Call"]').get_attribute("data-phone-number")
        except:
            Phone = '-'
        try:
            Website = x.find_element(By.XPATH , './/a[@aria-label="Website"]').get_attribute("href")
        except:
            Website = '-'




        data.append({'Business Name' :Business_Name ,'Rating':Rating ,'No of Reviews':No_of_Reviews ,'Phone Number':Phone ,'Website':Website })

y = 1
        
for i in range(1,100):
    sleep(2)
    get_data()
    
    print("Page {} scraped".format(i))
    try:
        element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Next"]')))
        driver.find_element(By.XPATH , '//button[@aria-label="Next"]').click()
    except:
        y = 0
        pass

    if y == 0 :
        print(" All results have been scraped successfully ")
        break
    
df = pd.DataFrame(data , columns=['Business Name','Website','Phone Number','Rating','No of Reviews'])
df.to_csv('{}_data.csv'.format(location),index=False)


# In[ ]:




