# with open('A_pythons.txt', 'r') as f:
#     text = f.read()
#     print(text)
#     print(len(text))
#     f.seek(10)
#     utext=f.read()
#     print(utext)

# with open('A_pythons.txt', 'r') as t:
#     l=t.read()
#     print(l)
#     t.seek(10)
#     ls=t.read(5)
#     print(ls)

# with open('A_pythons.txt','a') as i:
    # str=input("Enter String :")
    # i.write(str)
    # i.truncate(5)
    
with open('A_pythons.txt','r') as r:
    dt=r.read()
    print(dt)
