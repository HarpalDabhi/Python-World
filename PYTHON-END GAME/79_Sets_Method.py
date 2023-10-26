q={1,1,1,2,3,4,5,6}
print(q)

w={4,5,6,7,8,9}

x=q.union(w)

print(x)

y=q.intersection(w)
print(y)

print(q)

print(w)


print(q)

z={0,1,2,3,4,5}
z.add("Harpal")
print(z)

z.update(w)
print(z)

y={'a','b','c','d'}

z.update(y)
print(z)

z.remove('a')
print(z)

z.discard(0)
print("Furthure :")
print(z)

z.pop()
print("Last :")
print(z)

z.clear()
print(z)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
