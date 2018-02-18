#beautiful soup example

from bs4 import BeautifulSoup
import requests as rq
response=rq.get('https://www.crummy.com/software/BeautifulSoup/bs4/doc/')
doc=response.text
soup=BeautifulSoup(doc,'html.parser')
print(soup.prettify)