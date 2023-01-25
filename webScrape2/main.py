# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sqlite3
import requests
from bs4 import BeautifulSoup
import datetime

conn = sqlite3.connect("newDB")
c = conn.cursor()
#c.execute('''DROP TABLE cpu''')
c.execute('''CREATE TABLE cpu(date DATE, store TEXT, title TEXT, price REAL, stock TEXT)''')

def scrape(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    current_date = datetime.datetime.now()
    store = 'OVC'
    title = soup.find('h1').text.strip().replace('\n', '')
    price = soup.find('span', {'class': 'price__amount'}).text.replace('*', '').strip().replace('£', '')
    stock = soup.find('span', {'class': 'small d-inline-block ml-1'}).text.strip()
    c.execute('''INSERT INTO cpu VALUES(?,?,?,?,?)''', (current_date, store, title, price, stock))
    #print(current_date, store, title, price, stock)
    return


if __name__ == '__main__':
    scrape('https://www.overclockers.co.uk/amd-ryzen-9-3900x-twelve-core-4.6ghz-socket-am4-processor-retail-cp-3b5-am.html')
    conn.commit()

    c.execute('''SELECT * FROM cpu''')
    results = c.fetchall()
    print(results)

    conn.close()

