import numpy as np

arr=np.array([12,5,78,15],np.int64)

# print(arr)

# print(arr.dtype)

arr=np.array([[12,5,78,15]])

# print(arr[0][0])

arr[0][1]=20

print(arr)

larr=np.array([['A','B','C'],[1,2,3],['I','II','III']])

print(larr)

print(larr.dtype , larr.shape , larr.size)

# print(type(larr))