import requests
from bs4 import BeautifulSoup

# 1. GET THE HTML
url="https://hdabhi.netlify.app/"
R=requests.get(url)
# print(R)

HTML=R.content
# print(HTML)

# 2. PARSE THE HTML

Soup=BeautifulSoup(HTML,'html.parser')
# print(Soup)
# print(Soup.prettify)

# 3. HTML TREE TRAVERSAL

T=Soup.title
# print(T)
# print(type(T))

T=Soup.title.string
# print(T)
# print(type(T))

input=Soup.find_all('input')
# print(input)

# Function for the Tags

def tags(x):
    for i in x:
        print(i)
        print("\n")

# print(tags(input))

buttons=Soup.find_all('button')
# print(tags(buttons))

a=Soup.find_all('a')
# print(tags(a))

li=Soup.find_all('li')
# print(tags(li))

div=Soup.findAll('div')
# print(tags(div))

script=Soup.findChild('script')
# print(tags(script))

body=Soup.findChildren('body')
# print(tags(body))

a1=Soup.find('a')
# print(a1)

# print(Soup.find('i')['class'])

for i in a:
    if i.get('href')!='#':
        print(i.get('href'))
    else:
        pass

# print(Soup.find('p').get_text())

print("____________")

# print(Soup.find('div').get_attribute_list('class'))

# print(Soup)

# services=Soup.find(id="services")
# print(services)

print("____________")

# print(services.contents)

box=Soup.find_all('div',class_="box")
print(tags(box))

