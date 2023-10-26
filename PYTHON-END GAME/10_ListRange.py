a=['pratishya','prerna','palak','khusi','nisha','usha']
for i in a:
    print(i,end="❤️  ")

print("\n_________\n")
for i in range(len(a)):
    print(a[i],end="°  ")

for i in a:
    for j in i:
        print(j,end=" .")
    print("\n_________\n")

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]