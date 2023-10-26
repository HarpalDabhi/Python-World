import datetime

t=datetime.datetime.now()

print("Date :",t.date())

print(t.time())

print(t.day)

print(t.hour)

print(t.minute)

print(t.second)

print(t.microsecond)

print(t.month)

print(t.year)

print(t.weekday())

print(t.strftime('%d - %m -%y')) #24-2-2023

print(t.strftime('%d %b %Y'))  #24 feb 2015

print(t.strftime('%H : %M : %S %p')) # h : m : s : pm/am

print(t.strftime('%x')) #2/24/23

print(t.strftime('%X')) #h : m : s

