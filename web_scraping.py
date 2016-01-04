import requests
import html
from bs4 import BeautifulSoup
import re
##import schedule_feed
page = requests.get('http://www.krishnapath.org/free-ebooks-audiobooks-of-srila-prabhupada/life-comes-from-life/')
soup = BeautifulSoup(page.content,'html.parser')

print(soup.title)
##print(soup.find(id='fancy_image_load'))
links=soup.find_all('a',class_='fancy_image_load')

check = re.compile('.prc')
for link in links:
   print(link['href'])
   if re.search('.prc',str(link['href'])) is not None:
       book=requests.get(link['href'])
       print(book.content)
       f=open('a.prc','wb')
       f.write(book.content)
