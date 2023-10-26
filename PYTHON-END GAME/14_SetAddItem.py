a={1,2,3,4,5}

a.add(6)

print(a)

print(type(a))

b={7,8,9,10,11,12,13,14,15}

a.update(b)

print(a)

a.remove(5)
a.remove(10)
a.remove(15)
a.remove(11)
print(a)

a.discard(1)
a.discard(2)
a.discard(3)
a.discard(4)
a.discard(5)

print(a)


a.pop()
a.pop()
a.pop()
print(a)

a.clear()
print(a)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)