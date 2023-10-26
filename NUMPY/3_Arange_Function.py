import numpy as np

arg=np.arange(50)
print(arg)

rearg=arg.reshape(5,10)
print(rearg)

print(rearg[4][1])

print(arg)

arg=arg.reshape(5,10)
print(arg)

arg=arg.ravel()
print(arg)


