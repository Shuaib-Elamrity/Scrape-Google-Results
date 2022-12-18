#!/usr/bin/env python
# coding: utf-8

# In[123]:


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
options.add_argument("--headless")
from datetime import date

driver = webdriver.Chrome(options=options)
driver.maximize_window()


driver.get('https://www.google.com/localservices/prolist?g2lbs=AL1YbfU737UbBRHEQEDkntiZM8Nt8RfLAXuYIb5yhiksEj0okhm5Pev0nHZX9NoFpOFg-ICZqc3-Z_oGelwapjTHBnoEWd0W7fuIdIzI1PeJ5YTPCKt_kB8Y1uichea6zwIT4ZhzlPdB&hl=en-US&gl=us&cs=1&ssta=1&q=general%20contractors%20los%20angeles&oq=general%20contractors%20los%20angeles&slp=MgBSAggCYACSAa4CCgwvZy8xaGh3MDc1ODUKDS9nLzExZng3dzEzMHoKDS9nLzExYzFxbXRqNHEKDC9nLzExOXZieTdfZgoNL2cvMTFnbDEwX2pqaAoNL2cvMTFqN3ZmZ3lzNgoML2cvMTFoMGt4amp5Cg0vZy8xMWhfdnk3cDloCg0vZy8xMWpuZmhxeHZtCg0vZy8xMWgwdnIzZnpjCg0vZy8xMWZqczU1XzI0Cg0vZy8xMWJ2MmN6Zl9mCgsvZy8xdGZoencwMAoLL2cvMXRmN3h6eWQKDS9nLzExYjZ0X2tjX2wKDS9nLzExYmJybXk1ZzAKCy9nLzF0c2xqenlqCgwvZy8xMXhreGt4dmQKDS9nLzExaDI3eTc1Y2MKDS9nLzExajBuanNraGwSBBICCAESBAoCCAE%3D&src=2&origin=https%3A%2F%2Fwww.google.com&serdesk=1&sa=X&ved=2ahUKEwj8mdXRzYH8AhVvFjQIHcXdCgwQjGp6BAgYEAE&scp=ChdnY2lkOmdlbmVyYWxfY29udHJhY3RvchJNEhIJE9on3F3HwoAR9AhGJW_fL-IaEgkxzWQB0yrdgBEqOb3P1ih9gyILTG9zIEFuZ2VsZXMqFA3nxBYUFWGsRLkdBXV3FCUF75K5MAAaE2dlbmVyYWwgY29udHJhY3RvcnMiH2dlbmVyYWwgY29udHJhY3RvcnMgbG9zIGFuZ2VsZXMqEkdlbmVyYWwgY29udHJhY3Rvcg%3D%3D')

location = input("Please Enter The City : ")

element = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.XPATH, '//input[@type="search"]')))
    
search = driver.find_element(By.XPATH , '//input[@type="search"]')
search.clear()
search.send_keys("general contractors {}".format(location))

sleep(3)

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




