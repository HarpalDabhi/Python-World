def sqr(x):
    return x*x

cube = lambda y:y*y*y

li=[1,2,3,4,5,6,7,8,9,10]

print("List : ",li)

#Simple Trick
# li_1=[]
# for i in range(1,len(li)+1):
#     li_1.append(sqr(i))

# print("Updated :",li_1)



# Using Map Method
# li_2=map(cube,li)
# li_2=list(li_2)
# print("Cube :",li_2)



# Use of Filter Method

# def filter_li(y):
#     return y%2==0

# li_3=filter(filter_li,li)
# li_3=list(li_3)
# print("Filter :",li_3)

from functools import reduce

def add(m,o):
    return m+o

def mul(m,o):
    return m*o

li_5=reduce(mul,li)
print(li_5)

li_4=reduce(add,li)
print(li_4)

