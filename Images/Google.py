#!/usr/bin/env python
# coding: utf-8

#### Google


## Required Modules Installations

#!pip install lxml
#!pip install selenium
#!pip install bs4


## Import modules
import urllib.request    
from bs4 import BeautifulSoup    
from selenium import webdriver    
from selenium.webdriver.common.keys import Keys
import time    


##### Path ######################################################################
Chromedriver_PATH = 'c:\\chrome_webdriver\\chromedriver.exe'  # Chromedriver PATH 
save_path = 'd:\\images\\google\\'  #save_path 
#################################################################################


## get userdata & parameters
Search_Tag = input("Input Search_Tag : ")  # Search_Tag
scroll_cnt = int(input("Input scroll_cnt(minimim:5) : "))  #scroll count
scrolltime = float(input("Input scroll_sleep_second >>> range(5~10) : "))  #Sleep time 


## Get driver & open
driver = webdriver.Chrome(Chromedriver_PATH)  # Chromedriver PATH 
driver.get("https:\\www.google.co.kr\imghp?hl=ko&tab=wi&ei=l1AdWbegOcra8QXvtr-4Cw&ved=0EKouCBUoAQ")    
driver.maximize_window()
time.sleep(1)

## input Search_Tag & Submit
elem = driver.find_element_by_xpath("//*[@class='gLFyf gsfi']") 
elem.send_keys(Search_Tag)
time.sleep(1.5)  #Do not remove >> if you remove this line, can't go next step 
elem.submit()
time.sleep(3.0)  #Do not remove

############## Functions ################################################################################
def fetch_list_url():  #parsing src url
    imgList = soup.find_all("img", class_="rg_i Q4LuWd")
    for im in imgList:
        try :
            params.append(im["src"])                   
        except KeyError:
            params.append(im["data-src"])
    return params


def fetch_detail_url():  #save src to local  #changing save_path : Go to the top of this page (Path)
    for idx,p in enumerate(params,1):  #enumerate idx option 1 : get start index from 1 (default=0)
        urllib.request.urlretrieve(p, save_path + Search_Tag + '_' + str(idx) + "_google" + ".jpg")
###########################################################################################################    


## Crawling & Parsing
params=[]
for i in range(5):
    html = driver.page_source  #get source         
    soup = BeautifulSoup(html, "lxml") 
    params = fetch_list_url()  #save the img_url to params
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  #scroll
    time.sleep(scrolltime)


## Addtitional scrolling ('more results')
if scroll_cnt > 5:
    try : 
        driver.find_element_by_xpath("//*[@class='mye4qd']").click()  #click 'more results'
        for i in range(scroll_cnt-5):
            html = driver.page_source  #get source         
            soup = BeautifulSoup(html, "lxml") 
            params = fetch_list_url()  #save the img_url to params
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  #scroll
            time.sleep(scrolltime)
    except :
        print("Results are too short than requested scroll_cnt")
        
    
## Save imgs
print('')
print("Overlaped srcs : ", len(params))
params=list(dict.fromkeys(params))  #delete overlap  #index URL >> https://m31phy.tistory.com/130
fetch_detail_url()  #save img
print("Non_Overlap srcs : ", len(params))


driver.close()  #close browser 7

