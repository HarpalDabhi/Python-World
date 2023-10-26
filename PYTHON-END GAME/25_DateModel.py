import datetime
x=datetime.datetime.now()
print(x)

print(x.strftime('%d-%m-%Y'))

print(x.strftime('%a'))  # Day Name
print(x.strftime('%A')) # Full Name of Day

print(x.strftime('%b')) #Month Name
print(x.strftime('%B')) # Full Month Name

print(x.strftime('%I'))
print(x.strftime('%p'))
print(x.strftime('%X'))
