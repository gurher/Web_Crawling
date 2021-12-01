
import requests 
from bs4 import BeautifulSoup



url = 'https://www.indeed.com/jobs?q=python&limit=50'

indeed_result = requests.get(url)
indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser') 

pagination = indeed_soup.find("div", {"class":"pagination"})
# print(pagination)


pages = pagination.find_all('a')
spans = []
for page in pages:
    spans.append(page.find('span'))
    
# print(spans[:-1]) 

##2 4 Extracting Indeed Pages part Two

links = pagination.find_all('a')
pages = []
for link in links[:-1]:
    pages.append(int(link.string))


max_pages = pages[-1]
print(max_pages)


