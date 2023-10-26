# Pattern-1 Create the pattern as below and create the replica for the same so that it will create the diamond effect.

i=65
for j in range(1,6):
    for k in range(1,j+1):
        print(chr(i),end=" ")  
    print("\n")
    i+=1      