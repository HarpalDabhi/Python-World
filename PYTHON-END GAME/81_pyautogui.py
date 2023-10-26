import time
import pyautogui

import random

time.sleep(2)

i=0
while i<10:
    # pyautogui.typewrite(f"😴Good Morning!!! \n Jay Mataji \n have a great day !!! 😴")
    x=random.randint(999,9999)
    pyautogui.typewrite(f" OTP {x}")
    time.sleep(1)
    pyautogui.press("enter")
    # time.sleep(2)
    # pyautogui.hotkey("enter","ctrl","shift","]")
    
    i=i+1