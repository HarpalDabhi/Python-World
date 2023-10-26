import numpy as np

def ar_prop():
    arr=np.array([10000,20,30,40,50],np.int16)

    arr=np.array([[1,2,5,4],[12,20,50,60],[11,115,114,116],[1000,5000,9000,2000],[15120,151515,484815,784515]])
    print("Array : ",arr)
    print("Type of Array :",type(arr))
    print("Array Shape :",arr.shape)
    print("Array Data Type :",arr.dtype)
    print("Array Size :",arr.size)
    print("Array Max Argument :",arr.argmax())
    print("Array Minimum Argument :",arr.argmin())
    print(arr.argmin(axis=1))
    print(arr.argmin(axis=0))
    print(arr.argmax(axis=1)) # Row
    print(arr.argmax(axis=0)) # Column


def ar_creation():
    z=np.zeros((3,4))
    print(z)
    print(z.dtype)


def arng():
    arg=np.arange(25)
    print(arg)
    reshap=arg.reshape(25,1)
    print(reshap)
    print("___________")

    reshap=arg.reshape(5,5)
    print(reshap)
    print("___________")

    lspc=np.linspace(3,9,3)
    print(lspc)
    print("___________")

    emp=np.empty((5,5))
    print(emp)

    emp2=np.empty_like(reshap)
    print(emp2)
    print("___________")
    
def identity():
    idt=np.identity(4)
    print(idt)
    print("___________")

    idt2=np.ravel(idt)
    print(idt2)
    for i in range(len(idt2)):
        if idt2[i]==1:
            idt2[i]=5
    print(idt2)
    idt3=idt2.reshape(4,4)
    print(idt3)

def ar_operations():
    Q=np.arange(16)
    W=Q.reshape(4,4)
    print(W)
    print("Sum :",W.sum())
    print("Axis 0 means Columns :",W.sum(axis=0))
    print("Axis 1 menas rows :",W.sum(axis=1))

    T=W.T
    print(T)
    T=T.T
    print("Multiplication :",T*5)
    for itm in T.flat:
        print(itm,end=" -")
    print(T.ndim)
    print(W.ndim)
    print(W.size)
    print(W.shape)
    print("Bytes :")
    print(W.nbytes)

def arguments():
    X=np.arange(25)
    X=X.reshape(5,5)
    print(X)
    print(X.argmax())
    print(X.argmin())

    X=X.T
    print(X)
    print(X.argsort(axis=0))
    print("Axis - 1", X.argmax(axis=1))
    Y=X
    print(X+Y)
    print(X*Y)
    print("___")

    print([1,2,3]+[4,5,6])
    print(np.array([1,2,3])+np.array([4,5,6]))

def sqrt():
    O=np.arange(12)
    O=O.reshape(3,4)
    print(O)
    O=O.T
    print(O)
    print(np.sqrt(O))
    print(O.min())
    print(O.max())

    print(np.where(O>5))
    print(np.count_nonzero(O))
print(sqrt())