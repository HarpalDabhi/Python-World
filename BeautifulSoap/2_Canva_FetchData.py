import requests
from bs4 import BeautifulSoup

url="https://www.canva.com/"

r=requests.get(url)

html=r.content

print(html)