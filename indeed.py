
import requests 
from bs4 import BeautifulSoup

LIMIT = 50
URL = f'https://www.indeed.com/jobs?q=python&limit={LIMIT}'


def get_last_page():
         
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser') 
    pagination = soup.find("div", {"class":"pagination"} )    
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_pages = pages[-1]
    return max_pages

def extract_job(html):
    title = html.find("div", {"class": "heading4"}).find("span", title=True).string
    # title = html.find('h2',{"class": ["jobTitle jobTitle-color-purple","jobTitle jobTitle-color-purple jobTitle-newJob"]}).text    
    location = html.find("div", {"class" : "companyLocation"}).text
    # location = html.find("div", {"class" : "recJobLoc"})["data-rc-loc"]
    company = html.find("span", {"class":"companyName"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()
    job_id = html.parent["data-jk"]
    return { 
        'title' : title , 
        'company' : company, 
        'location' : location,
        'link' :f"https://www.indeed.com/viewjob?jk={job_id}"
        }

def extract_jobs(last_pages):
    jobs = []
    for page in range(last_pages):
        
        print(f"scrapping page {page}")
        
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all('div', {"class":"slider_container"})   #     #job_seen_beacon
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs        
        

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs 