
from email.mime import base
from requests import get 
from selenium import webdriver
from bs4 import BeautifulSoup
                                 
browser = webdriver.Chrome(executable_path= '/Users/edward/Documents/Web_Scraping/Jobs/Indeed/chromedriver')                                                                     

 
def get_page_count(search_term='python', location='California'):
    base_url = f"https://www.indeed.com/jobs?q={search_term}&l={location}&from=searchOnHP&vjk=de2c067e43d5b964"

    browser.get(base_url)


    soup = BeautifulSoup(browser.page_source, 'html.parser')
    
    
    pagination = soup.find("nav", {"class":"css-jbuxu0 ecydgvn0"}) 
    
    print(pagination)
    # pagination = soup.find("ul", class_="pagination-list")
    if pagination == None:
        return 1
    pages = pagination.find_all("li", recursive = False)
    count = len(pages)
    if count >=5:
        return 5
    else:
        return count

print(get_page_count('python', 'California'))


# def extract_indeed_jobs(search_term='python', location='California'):

#     base_url = f"https://www.indeed.com/jobs?q={search_term}&l={location}&from=searchOnHP&vjk=de2c067e43d5b964"


#     browser.get(base_url)


#     soup = BeautifulSoup(browser.page_source, 'html.parser')
#     job_list = soup.find("ul", class_= 'jobsearch-ResultsList')
#     jobs = job_list.find_all('li', recursive=False)

#     results = []
#     for job in jobs:
#         zone = job.find('div', class_="mosaic-zone")
#         if zone == None:
#             anchor = job.select_one("h2 a")
#             title = anchor['aria-label']
#             link = anchor['href']
#             company = job.find('span', class_="companyName")
#             location = job.find("div", class_="companyLocation")
            
#             job_data = {
                
#                 'link' : f"https://www.indeed.com{link}",
#                 'company' : company.string,
#                 'location' : location.string ,
#                 'position' : title
                    
#             }
#             results.append(job_data)
            
#     for result in results:
#         print(result, "\n//////\n")
            