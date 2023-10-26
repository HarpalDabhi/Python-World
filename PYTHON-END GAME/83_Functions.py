def print_me():
    print("_____\n")

print_me()

def circle(x):
    print("Area : ",x*x*3.14)

circle(10)

circle(15)

def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)
    
print(fact(4))
print(fact(5))