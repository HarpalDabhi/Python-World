import numpy as nmp

zeros=nmp.zeros((2,5))
# print(zeros)

lspc=nmp.linspace(3,15,5)  #(initial,end,partition)
# print(lspc)

lspc=nmp.linspace(0,1,5)
# print(lspc)

emp=nmp.empty((3,2))
# print(emp)

emplike=nmp.empty_like(lspc)
# print(emplike)

idt=nmp.identity(5)
print(idt)

def unitarr(x):
    for i in range(5):
        for j in range(5):
            # print(idt[i][j])
            if idt[i][j]==1:
                idt[i][j]=x
    else:
        print("DONE")

unitarr(12)
print(idt)

print(idt.shape, idt.dtype, idt.size)
