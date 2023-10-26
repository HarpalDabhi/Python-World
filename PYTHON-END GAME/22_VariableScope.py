def run():
    x=50
    print(x)
print(run())
x=None
print(x)

x=123
def you():
    global x
    x=12
(you())
# print("best")
print(x)