# for i in range(10):
#     for j in range(10):
#        print(j,end="  ")         #i=0 and j>=4
#     print("\n")   


for i in range(11):
    for j in range(10):
        if i==0 and j<5:
            print(" ",end=" ")
        if i==0 and j>=5:
            print("*",end="  ")
        if j!=5 and i>0:
            print(" ",end=" ")
        if j==5:
            print("*",end=" ")
        if i==5:
            print("*",end=" ")   
    print("\n")   
                      
