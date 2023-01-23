# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from urllib.request import urlopen
import re

def scraper():
    url = "http://olympus.realpython.org/profiles/aphrodite"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print(html)
    title_index = html.find("<title>")
    start_index = title_index + len("<title>")
    end_index = html.find("</title>")
    title = html[start_index:end_index]
    print(title)
    print(start_index)
    print(end_index)

def scraper_new():
    url = "http://olympus.realpython.org/profiles/dionysus"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    print(html)

    pattern = "<title.*?>.*?</title.*?>"
    match_results = re.search(pattern, html, re.IGNORECASE)
    title = match_results.group()
    title = re.sub("<.*?>", "", title)  # Remove HTML tags

    print(title)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #scraper()
    scraper_new()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
