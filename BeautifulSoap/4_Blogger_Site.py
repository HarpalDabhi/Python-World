import requests
from bs4 import BeautifulSoup

def tags(x):
    for i in x:
        print(i)
        print("\n")

url="https://www.blogger.com/"
reqst=requests.get(url)
htm=reqst.content
sp=BeautifulSoup(htm,'html.parser')
title=sp.title
link=sp.find_all('link')
# print(sp.find('a')['class'])
# for i in link:
#     print(i.get('rel'))

h2=sp.find_all('h2')

for i in h2:
    print(i.get_text())

