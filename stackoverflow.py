import requests
from bs4 import BeautifulSoup 

LIMIT  = 50
URL = f'https://stackoverflow.com/jobs?q=data'   #&pg={pages}'


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find( 'div', {"class": "s-pagination"} )
    pages = pagination.find_all('a')
    pages = pages[-3]
    last_page = pages.get_text().strip()   # get_text(strip=True)
    return int(last_page)





def extract_jobs(last_page):
    jobs = []
    for page in range(1):
        result = requests.get(f'{URL}&pg={page+1}')
        soup = BeautifulSoup(result.text, 'html.parser')
        titles = soup.find_all('h2', {'class' : "mb4 fc-black-800 fs-body3"} )
        company_location = soup.find_all('h3',{"class" : "fc-black-700 fs-body1 mb4"})

        for result, company in zip( titles, company_location):
            title = result.find('a')['title']
            company_name = company.find('span')
            location = company.find('span', {"class" : "fc-black-500"})
            # company_name.text, location.text)
            result = {
                        "title" : title, 
                        "company_name" : company_name.text.strip() ,
                        "location" : location.text.strip()                        
                      }
            jobs.append(result)
    return jobs        


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return []
