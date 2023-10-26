import requests

from bs4 import BeautifulSoup



url="https://www.w3schools.com/"

r=requests.get(url)

htmlContent=r.content

print(htmlContent)

# 2. Parse the HTML

soup=BeautifulSoup(htmlContent,'html.parser')

# print(soup)

title=soup.title

# print(title)

para=soup.find_all('div')
# print(para)

# print(soup.find('a')['class'])

# print(soup.find('div'))
# print(soup.find('div')['id'])
# print(soup.find('div')['style'])

# print(soup.find('p').get_text())
# print(soup.find('p'))

