Q=["Harpal","Vishal","Purvi","Kinjal","Janaki"]
print(Q)
print(Q[1])
print(Q[::-1])
print(Q[3:])
print(type(Q))

if "Harpal" in Q:
    print("harpal exists")

Q.insert(0,"Gopi")
print(Q)

Q.append("Love")
print(Q)

G=["Manisha","Myushi","Prerna","Krishna"]

B=["Harpal","Vipul","Malay","Jayraj"]

G.extend(B)

print(G)

G.remove("Myushi")
print(G)

G.pop(1)
print(G)

G.pop()
print(G)

R=[12,4,5,78,89,4,4,12,45]
sum=0
for i in R:
    print(i)
    print("Sqe : -- >",i*i)
    sum=i+sum
print(sum)