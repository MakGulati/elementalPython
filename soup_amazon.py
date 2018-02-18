#!/usr/bin/env python3
import requests as rq
from bs4 import BeautifulSoup

response=rq.get('https://www.amazon.in/s/ref=nb_sb_ss_i_1_4?url=search-alias%3Dgrocery&field-keywords=blueberries+dried&sprefix=blue%2Cgrocery%2C308&crid=3B69N5S2GA4LK')
html_text=response.text
soup=BeautifulSoup(html_text,'html.parser')


#with open('amaz.txt',"w") as fp:
#    fp.write(soup.prettify())
#    
#print(soup.prettify())
tag_a_class=soup.find_all("a", class_="a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal")
#tag_span_price=soup.find_all("span", class_="a-price-whole")
tag_span_price=soup.find_all("span",class_="textContainer__text")
#for div in soup.findAll('a', attrs={'class':'a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal'}):
#    print(div.index,div)

for n in range(len(tag_a_class)):

    item_link=tag_a_class[n]['href']
    item_name=tag_a_class[n]['title']
    item_price=tag_a_class[n]
    item_name=item_name.strip(",")
    item=item_link+","+item_name+"\n"
    with open('dbfile.csv','a') as f:
        f.write(item)

#print(tag_span_price[24].string) 

print((tag_span_price))
      
#for n2 in range(len(tag_span_price)):
#    print(tag_span_price[n2]['price'])    


