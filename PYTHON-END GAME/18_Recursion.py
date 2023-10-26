def fact(n):
    if n>0:
      result= n * fact(n-1)  #5*4*3*2*1
      return result
    elif n==1 or n==0:
        return 1

print(fact(5))