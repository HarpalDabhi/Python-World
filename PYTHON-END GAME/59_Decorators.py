
# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("Good Morning Sir !")
#         fx(*args, **kwargs)
#         print("Thanks for Using this Function!")
#     return mfx

# @greet
# def hello():
#     print("Hello Harpal !")  # Here the hello is decorated by @greet

# hello()
# print("\n\n")
# greet(hello())

# print("\n_____________\n")
# @greet
# def add(a,b):
#     print("Add :",a+b)

# add(10,20)

# greet(add(50,40))

def letter(fx):
    def mletter():
        print("Hi ...")
        fx()
        print("...Bye")
    return mletter

@letter
def purpose():
    print("I am your Best Purpose")

# letter(purpose())

purpose()