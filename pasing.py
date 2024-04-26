from bs4 import BeautifulSoup
import requests
from db import insert_data

url = 'https://asaxiy.uz/product/kompyutery-i-orgtehnika/noutbuki/noutbuki-2'
data = requests.get(url).text


soup = BeautifulSoup(data, 'html.parser')
main_block = soup.find('div', class_='row')
block = main_block.find_all('div', class_='col-6')
for product in block:
    image = product.find('img', class_='img-fluid')['data-src']
    product_name = product.find('span', class_='product__item__info-title').get_text()
    str_product_name = str(product_name).strip()
    product_price = product.find('span', class_='product__item-price').get_text()
    product_month = product.find('div', class_='installment__price').get_text()
    data_month = str(product_month)
    one_month = data_month.split(' ')
    one_month_price = one_month[0] + ' ' +  one_month[1]
    year_price = one_month[-2] + ' ' + one_month[-1]
    kredit = f"1 oy uchun to'lanadigan narx -> {one_month_price}\nTolov muddati: {year_price}"
    insert_data(product_name, image, product_price, one_month_price)
print(insert_data)


