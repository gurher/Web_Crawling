
from requests import get 
from selenium import webdriver
from bs4 import BeautifulSoup
                                 
browser = webdriver.Chrome(executable_path= '/Users/edward/Documents/Web_Scraping/Jobs/Indeed/chromedriver')                                                                     

 
search_term = 'python'
location = 'California'
page = 0

base_url = f"https://www.indeed.com/jobs?q={search_term}&l={location}&from=searchOnHP&vjk=9e42edea9c385922"


browser.get(base_url)


soup = BeautifulSoup(browser.page_source, 'html.parser')

# for a in soup:
#     print(a.find('ul', class_="jobsearch-resultsList"))



