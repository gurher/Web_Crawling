#!/usr/bin/env python
# coding: utf-8

# ### Instagram

## Required Modules Installations

#!pip install lxml
#!pip install selenium
#!pip install bs4


## Import modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib.request
from time import sleep
import time as time
import getpass


##### Path ######################################################################
Chromedriver_PATH = 'c:\\chrome_webdriver\\chromedriver.exe'  # Chromedriver PATH 
save_path = 'D:\\images\\instagram\\'  #save_path 
#################################################################################


## get userdata & parameters
username = input("Input ID : ")  # User ID
password = getpass.getpass("Input PWD : ")  # User PWD  #getpass : hidden option
hashTag_k = input("Input HashTag # : ")  # hashTag
scroll_cnt = int(input("Input scroll_cnt : "))  #scroll count
scrolltime = float(input("Input scroll_sleep_second >>> range(5~10) : "))  #Sleep time 
hashTag = '#' + hashTag_k


## Get driver & open
driver = webdriver.Chrome(Chromedriver_PATH)  # Chromedriver PATH 
driver.get("https://www.instagram.com/accounts/login/")
hashLink = '//a[@href="/explore/tags/'+hashTag+'/"]'
driver.maximize_window()
sleep(3)


## insert logindata in "login div"
element_id = driver.find_element_by_name("username")
element_id.send_keys(username)
element_password = driver.find_element_by_name("password")
element_password.send_keys(password) 
driver.implicitly_wait(5)

## click login botton
driver.find_element_by_css_selector('.sqdOP.L3NKy.y3zKF').click()

## input hash tag & push 'Enter'x2
time.sleep(10)  #recommand not to change times
search = driver.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input""")
search.send_keys(hashTag)
time.sleep(5)  #recommand not to change times
search.send_keys(Keys.ENTER)
search.send_keys(Keys.ENTER)
time.sleep(10)  #recommand not to change times


############## Functions ################################################################################
def fetch_list_url():  #parsing src url
    imgList = soup.find_all("img", class_="FFVAD")
    for im in imgList:
        try :
            params.append(im["src"])  
        except KeyError:
            params.append(im["srcset"])
    return params


def fetch_detail_url():  #save src to local  #changing save_path : Go to the top of this page (Path)
    for idx,p in enumerate(params,1):  #enumerate idx option 1 : get start index from 1 (default=0)
        urllib.request.urlretrieve(p, save_path + hashTag_k + '_' + str(idx) + "_instagram" + ".jpg")
###########################################################################################################    
    

## Crawling & Parsing
params=[]
for i in range(scroll_cnt):
    html = driver.page_source  #get source         
    soup = BeautifulSoup(html, "lxml") 
    params = fetch_list_url()  #save the img_url to params
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  #scroll
    time.sleep(scrolltime)
    

## Save imgs
print('')
print("Overlap srcs : ", len(params))
params=list(dict.fromkeys(params))  #delete overlap  #index URL >> https://m31phy.tistory.com/130
fetch_detail_url()  #save img
print("Non_Overlap srcs : ", len(params))


driver.close()  #close browser

