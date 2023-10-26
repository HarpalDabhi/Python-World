#  Is  vs  '=='

# is check the location and '==' check the value

# 1.
a=4
b="4"

# print(a==b) #F
# print(a is b) #F

a=[1,2,3]
b=[1,2,3]

# print(a==b) # True
# print(a is b) # False

a=[1,2,3,4]
b=a

# print(a==b) # True
# print(a is b) # True

a=4
b=4

# print(a==b) # T
print(a is b) # T

a="Harpla"
b="Harpla"

print(a==b) #
print(a is b) #

a={'x':10,'y':20}
b={'x':10,'y':20}

print(a==b) #
print(a is b) #

