friends=['malay','jaylo','kuldip','ilesh','kiran','krishna','ram','laxman','me','harpal']

print(friends[5])
print(friends[-1])

print(friends[5:])
print(friends[1:5])

print(friends[::-1])  # this will reverse the order of friends

print('krishna' in friends)

a=[0,1,2,3,4,5,6,7,8,9]
b=[11,12,13,14,15,16,17,18,19]
a.extend(b)
print(a)

tip=("Love",'Kush')
a.extend(tip)
print(a)