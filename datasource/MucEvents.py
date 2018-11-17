
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
dates = []
links =[]
count = 0
startdate = "29.11.2018" #Need Date query
enddate = "22.12.2018"   #Need Date query
response = get('https://www.muenchen.de/veranstaltungen/event/listing.html?what=&where=&from=' + startdate + '&to=' + enddate, headers = basicHeaders)
html_soup = BeautifulSoup(response.text, 'lxml')
if html_soup is not None:
        eat_containers = html_soup.find_all('div', class_= ['item'])

        for container in eat_containers:
            if count <= 5:
                count = count + 1

                name = container.h2.text
                names.append(name)
                print(name)

                date = container.div.span.text.split('\n')[1].strip()#find('span', attrs = {'data-reactid': '.0.0.$6259.0.1.1.0'})
                dates.append(date)
                print(date)

                address = container.div.find('a', class_ = 'eventinfo eventinfo--location').text
                addresses.append(address)
                print(address)

                link = container.div.find('a', attrs = {'class': 'eventinfo eventinfo--headline'})['href']
                links.append(link)
                print(link)




test_df = pd.DataFrame({'Events': names,'link':links, 'Location':addresses, 'Time':dates})
test_df.to_csv('mucevents.csv')
test_df.to_json('mucevents.json')
print(test_df.info())