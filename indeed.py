
import requests 
from bs4 import BeautifulSoup

LIMIT = 50
URL = 'https://www.indeed.com/jobs?q=python&limit={LIMIT}'


def extract_indeed_pages():
         
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser') 
    pagination = soup.find("div", {"class":"pagination"} )    
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_pages = pages[-1]
    return max_pages


def extract_indeed_jobs(last_pages):
    jobs = []
    # for page in range(last_pages):
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all('div', {"class":"job_seen_beacon"})
    for result in results:
        title = result.find('h2',{"class": "jobTitle jobTitle-color-purple"}).find("span")['title']
        company = result.find("span", {"class":"companyName"})
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
        company = company.strip()
        print(title, company)
        
     #  print(title.find("span").string)  #{"class":"title"})
        
            # return jobs
    