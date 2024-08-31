import requests
import pandas
from bs4 import BeautifulSoup

lumia = requests.get("https://www.jumia.com.ng/flash-sales/?sort=newest#catalog-listing")
print(lumia.status_code)

src = lumia.content
soup = BeautifulSoup(src, 'html.parser')  # parsing is converting from one format to another

articles = soup.findAll(class_='info')

product_data = []
for data in articles:
    product_data.append(data.get_text())
    print(data.get_text())
# print(product_data)
# edited_data = [data.replace('%', '% ') for data in product_data]
#print(edited_data)


