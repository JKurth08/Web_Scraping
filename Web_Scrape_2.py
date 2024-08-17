import requests
from bs4 import BeautifulSoup
import re

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id = "ResultsContainer")
job_elements = results.find_all("div", class_ = "card-content")

for job_element in job_elements:
    title = job_element.find("h2", class_ = "title")
    company = job_element.find("h3", class_ = "company")
    location = job_element.find("p", class_ = "location")
    # print(f"{title.text.strip()}\n{company.text.strip()}\n{location.text.strip()}\n")

# python_jobs = results.find_all("h2", string = "Python")
    # ^ this is getting changed to a lambda function 

python_jobs = results.find_all("h2", string = lambda text: "python" in text.lower())

# staging changes to test bash script

# list comprhension that operates on each level of <h2> titles
# in python_jobs
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# re-writing the for loop above to search through 'python_jobs'
for job_element in python_job_elements:
    title = job_element.find("h2", class_ = "title")
    company = job_element.find("h3", class_ = "company")
    location = job_element.find("p", class_ = "location")
    # this gives an error; why is this?
    print(f"{title.text.strip()}\n{company.text.strip()}\n{location.text.strip()}")
    links = job_element.find_all("a")
    for link in links:
        full_url = link["href"]
        if link.text == "Apply":
            print(f"{link.text}: {full_url}")
    print()                   

# changing from testing_2
