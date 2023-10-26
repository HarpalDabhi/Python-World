def hello():
    print("Hello I love Hello ")

hello()
hello()

def love(name):
    print(f"My Friend name is {name}.")

love("harpal")
love("vishal")
love("sahil")
love("malay")
love("harpal")

def myfunc(*friend):
    print(friend[5])

myfunc("Harpal",'Manish','Pranav','Krishna','Jadav','Jay')

def new(love="Priyanshi"):
    print(f"You my best {love}")

new("Harpal")
new()

def sqr(x):
    return x*x

print(sqr(10))
print(sqr(8))

def sum(x,y):
    sum=x+y
    return sum

print(sum(15,20))
