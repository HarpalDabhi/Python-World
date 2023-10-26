dict_1={
    'H':2003,
    "V":2006,
    'K':2005
}

print(dict_1['H'])
x=0
for i in dict_1:
    print(dict_1[i])
    x+=1

print(x)

print(len(dict_1))

x=dict_1.get('H')
print(x)

x=dict_1.get('X')
print(x)

x=dict_1['H']
print(x)
# x=dict_1['x']
# print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

print(car.items())

print(car.keys())
print(car.values())

car['Love']='Gopi'

print(car)

car.update({'God':'Krishna'})

car.pop('brand')
car.popitem()

car.clear()
print(type(car))
print(car)

a={1,2}
print(type(a))
a.clear()
print(a)
print(type(a))

