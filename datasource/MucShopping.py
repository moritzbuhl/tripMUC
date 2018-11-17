
from bs4 import BeautifulSoup

from requests import get
import pandas as pd

basicHeaders = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.9',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
 }

names = []
addresses = []
ratings = [] 
links = []
zipcodes = []
pages = ["second-hand", "einkaufszentren", "einkaufspassagen", "outlets"]
for page in pages:

    response = get('https://www.muenchen.de/shopping/' + page + '.html', headers = basicHeaders)
    html_soup = BeautifulSoup(response.text, 'lxml')
    if html_soup is not None:
        eat_containers = html_soup.find_all('div', class_= ['item item--premium','item item--business'])

        for container in eat_containers:
            if container.div.find('span', class_ = 'item__url item__url--address str') is not None:

                name = container.h3.text.split('\n')[1].strip()
                names.append(name)

                address = container.div.find('span', class_ = 'item__url item__url--address str').text
                addresses.append(address)

                zipcode = container.div.find('span', class_ = 'item__url item__url--address zip').text[0:5]
                zipcodes.append(zipcode)
                print(zipcode)

                rating = container.find('div', attrs = {'class':'rating'})['data-avgrating']
                ratings.append(rating)

                link = container.div.find('a', attrs = {'class': 'item__url'})['href']
                links.append(link)




test_df = pd.DataFrame({'restaurant': names, 'address': addresses, 'votes': ratings, 'link':links, 'Zipcode':zipcodes})
test_df.to_csv('mucshopping.csv')
test_df.to_json('mucshopping.json')
print(test_df.info())