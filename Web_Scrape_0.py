# first project in python / VS

from urllib.request import urlopen
import re

# basic snippet to open and read the source code of a website (in HTML)
url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
html = page.read().decode("utf-8")

# searching for text in website
title_index = html.find("<title>")
start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index : end_index]

# reg expressions
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<TITLE.*?>.*?</title.*?>"
match_result = re.search(pattern, html, re.IGNORECASE)
title = match_result.group()
formatted_title = re.sub("<.*?>", "", title)


""" 
# Write a program that grabs the full HTML from the following URL:
>>> url = "http://olympus.realpython.org/profiles/dionysus"
"""

def main_function() -> object:
    url = "http://olympus.realpython.org/profiles/dionysus"
    page = urlopen(url)
    html = page.read().decode("utf-8")

    name_pattern = "<h2>Name:.*?</h2>"
    match_result = re.search(name_pattern, html, re.IGNORECASE)
    name = match_result.group()
    fomatted_name = re.sub("<.*?>", "", name)

    fav_color_index = html.find("Favorite Color: ")
    fav_color_index_offset = html[fav_color_index : ].find("<")
    formatted_fav_color = html[fav_color_index : fav_color_index + fav_color_index_offset]
    print(formatted_fav_color)


if __name__ == "__main__":
    main_function()
