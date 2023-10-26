import time
import pyautogui

time.sleep(5)


# i=1
# while i<=5:
#     pyautogui.typewrite("Hi Bro")
#     time.sleep(0)
#     pyautogui.press("enter")
#     i=i+1

import requests

from bs4 import BeautifulSoup



url="https://www.w3schools.com/"

r=requests.get(url)

htmlContent=r.content

# print(htmlContent)

soup=BeautifulSoup(htmlContent,"html.parser")
# print(soup)

a=soup.find_all('link')
# print(a)

a=list(a)

time.sleep(5)

i=0
while i<len(a):
    pyautogui.typewrite(a[i])
    print(a[i])
    time.sleep(0)
    pyautogui.press("enter")
    i=i+1

