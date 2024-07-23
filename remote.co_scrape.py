# New Project: Remote.co Scrape -> 6-29-24
# URL: https://remote.co/remote-jobs/developer/

from bs4 import BeautifulSoup
import requests

url = "https://remote.co/remote-jobs/developer/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

page_content = soup.find(class_ = "container pt-4")
job_elemnts_1 = page_content.find(class_ = "card bg-white m-0")
job_elements_2 = job_elemnts_1.find_all(class_ = "col position-static")

job_elements_3 = page_content.find_all(class_ = "card bg-white m-0")

# first, lets find a list of all the job titles in this database
def find_all_jobs() -> list:

    for job in job_elements_3:
        all_job_titles = job.find(class_ = "p-3 m-0")
        link = all_job_titles.find("a")["href"]
        full_url = url[0:17] + link
        page = requests.get(full_url)
        soup = BeautifulSoup(page.content,  "html.parser")
        page_1_content = soup.find(class_ = "card-body")
        links = page_1_content.find_all("a", class_ = "rounded-sm mx-1 mb-1 btn-category d-inline-block")
        url_list = []

        for link in links:
            full_url = url[0:17] + link["href"]
            url_list.append(full_url)
    
    url_list.pop(0) 
    url_list.pop(17)
    
    all_jobs = []
    for link in url_list:
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")
        page_content = soup.find(class_ = "container pt-4")
        page_content_1 = page_content.find(class_ = "card bg-light mb-3 rounded-0")
        job_titles = page_content_1.find_all(class_ = "font-weight-bold larger")
        for job_title in job_titles:
            all_jobs.append(job_title.text)
    
    return all_jobs

if __name__ == "__main__":
    print(find_all_jobs())
# lets try and search for jobs given key words

# all jobs that contain the word 'software'

