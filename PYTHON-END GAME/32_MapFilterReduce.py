import random
li=[]

for i in range(10):
    x=random.randint(5,20)
    li.append(i)
    li[i]=x

print(li)

sqr=lambda n:n*n

li2=list(map(sqr,li))
print(li2)

def evenOdd(y):
    return y%2==0

li3=list(filter(evenOdd,li))
print(li3)

li4=list(filter(evenOdd,li2))
print(li4)

from functools import reduce

def add(x,y):
    return x+y

li5=(reduce(add,li))
print(li5)

print(reduce(add,li2))

print(reduce(add,li3))
print(reduce(add,li4))