# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from urllib.request import urlopen

def scraper():
    #driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    products = []
    prices = []
    ratings = []

    url = "https://www.flipkart.com/search?count=40&otracker=CLP_filters&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D5000&p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkJ1ZGdldCBQaG9uZXMgQmVsb3cg4oK5NTAwMCJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D&wid=2.productCard.PMU_V2_2"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    # print(soup.find_all("img"))
    for a in soup.findAll('a', href=True, attrs={'div class': '_36fx1h _6t1WkM _3HqJxg'}):
        name = a.find('div', attrs={'class': '_13oc-S'})
        rating = a.find('div', attrs={'class': '_3LWZ1K'})
        price = a.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
        products.append(name.text)
        ratings.append(rating.text)
        prices.append(price.text)
        #print("Yes")
    #print(products)
    #print(ratings)
    #print(prices)
    df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
    df.to_csv('products.csv', index=False, encoding='utf-8')

if __name__ == '__main__':
    scraper()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
