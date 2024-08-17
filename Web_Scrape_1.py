from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, "html.parser")

formatted_text = soup.get_text()
img1, img2 = soup.find_all("img")

"""
Write a program that grabs the full HTML from the 
page at the URL http://olympus.realpython.org/profiles.

Using Beautiful Soup, print out a list of all the links on 
the page by looking for HTML tags with the name 'a' and 
retrieving the value taken on by the href attribute of each tag.
"""
url = "http://olympus.realpython.org"
page = urlopen(url + "/profiles")
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, "html.parser")

a_tags = soup.find_all("a")
for i in range(len(a_tags)):
    full_url = url + a_tags[i]["href"]
    print(full_url)

# also changing file
