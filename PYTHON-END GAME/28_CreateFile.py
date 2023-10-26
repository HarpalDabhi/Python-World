# f=open('Harpal2.txt','a')
# data=f.write("I love You\n")
# print(data)
# f.close()

# with open('Harpal2.txt','r') as x:
#     dt=x.read()
#     udt=x.seek(5)
#     print(dt)
#     print(udt)
#     dt2=x.read()
#     print(dt2)

    #seek will cut 5

with open('Harpal2.txt','a') as x:
    # d=x.read()
    # print(d)
    x.truncate(10)