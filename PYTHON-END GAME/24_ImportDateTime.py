import datetime

x=datetime.datetime.now()
print(x)

print(x.year)
print(x.day)
print(x.month)
print(x.second)
print(x.microsecond)
print(x.minute)
print(x.hour)

print(x.strftime('%d-%m-%Y'))