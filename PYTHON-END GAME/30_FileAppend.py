f=open('Harpal.txt','a')
a=int(input())
for i in range(1,11):
    f.write(f" \n{a} X {i} ={a*i}")
f.close()