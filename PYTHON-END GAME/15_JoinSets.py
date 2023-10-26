a={1,2,3,4,5,6,7,8,9}

b={2,4,6,8,10,12,14}

c=a.union(b)
print(c)

print(a)

a.update(b)

print(a)

a.intersection_update(b)
print(a)

a={10,20,30,40,50,60}

b={10,20,30,40,50}

a.symmetric_difference_update(b)
print(a)

x=b.symmetric_difference(a)
print(x)
