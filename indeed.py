
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
    
print(spans[:-1]) 



