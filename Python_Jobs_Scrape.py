# practicing going through a static website and scraping it
# website in use: https://pythonjobs.github.io/

import requests
from bs4 import BeautifulSoup

url = "https://pythonjobs.github.io/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# find title of a job post
page_content = soup.find(id = "container")
job_elemnts = page_content.find_all(class_ = "job_list")


# finding every job title and printing a list:
def find_job_title() -> list:
    for job in job_elemnts:
        job_titles = job.find_all("h1")
        Job_title_list = []
        for job_title in job_titles:
            job_title = job_title.text
            Job_title_list.append(job_title)
    return Job_title_list
    

# find details of job; location, company, etc...
        
# Loacation
def find_job_location() -> list:
    job_location_list = []           
    for job in job_elemnts:
        job_locations = job.find_all("i", class_ = "i-globe")
        for job_location in job_locations: 
            job_location = job_location.parent.text
            job_location_list.append(job_location)
    return job_location_list

# Date
def find_job_date() -> list:
    job_date_list = []
    for job in job_elemnts:
        job_dates = job.find_all("i", class_ = "i-calendar")
        for job_date in job_dates:
            job_date = job_date.parent.text
            job_date_list.append(job_date)
    return job_date_list

# Type of Position
def type_of_position() -> list:
    job_position_list = []            
    for job in job_elemnts:
        job_positions = job.find_all("i", class_ = "i-chair")
        for job_position in job_positions:
            job_position = job_position.parent.text
            job_position_list.append(job_position)
    return job_position_list

# Company
def find_company() -> list:
    company_list = []
    for job in job_elemnts:
        job_companies = job.find_all("i", class_ = "i-company")
        for job_company in job_companies:
            job_company = job_company.parent.text
            company_list.append(job_company)
    return company_list

# Job Details
# this might take some extra digging... full details within second link
def job_detail() -> list: 
    detail_text = []
    for job in job_elemnts:
        deatail_links = job.find_all("a", class_ = "go_button")
        for detail_link in deatail_links:
            # [:-1] deletes the last '/' in the URL
            detail_link = url[:-1] + detail_link["href"]
            detail_page = requests.get(detail_link)
            detail_soup = BeautifulSoup(detail_page.content, "html.parser")
            detail_page_content = detail_soup.find(id = "container")
            detail_elements = detail_page_content.find_all("p")
            more_detail_elements = detail_page_content.find_all("li")
            detail_elements += more_detail_elements
            for detail_element in detail_elements:
                # print(f"\n{detail_element.text}\n")
                detail_text.append(detail_element.text)
    global detail_length 
    detail_length = len(detail_text)
    return detail_text

if __name__ == "__main__":
    for detail in job_detail():
        print(detail)
    print(detail_length)
        
# lets see if this works