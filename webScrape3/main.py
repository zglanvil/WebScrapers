# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from requests_html import HTMLSession

s = HTMLSession()


def get_product_links(page):
    url = f'https://themes.woocommerce.com/storefront/product-category/clothing/page/{page}'
    r = s.get(url)
    products = r.html.find('ul.products li')
    links = []
    for item in products:
        links.append(item.find('a', first=True).attrs['href'])
    return links


def parse_product(url):
    # test = 'https://themes.woocommerce.com/storefront/product/lowepro-slingshot-edge-250-aw/'
    r = s.get(url)
    if r.html.find('h2.woocommerce-loop-product__title'):
        title = r.html.find('h2.woocommerce-loop-product__title', first=True).text.strip()
    elif r.html.find('h1.product_title.entry-title'):
        title = r.html.find('h1.product_title.entry-title', first=True).text.strip()
    price = r.html.find('p.price', first=True).text.strip().replace('\n', '')
    cat = r.html.find('span.posted_in', first=True).text.strip()
    try:
        sku = r.html.find('span.sku', first=True).text.strip()
    except AttributeError as err:
        sku = 'None'

    product = (title, price, sku, cat)
    return product


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for x in range(1, 4):
        urls = get_product_links(x)
        for url in urls:
            print(parse_product(url)) #at this point can pass tuple into database

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
