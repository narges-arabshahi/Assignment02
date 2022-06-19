import math
fib=[]
n=int(input("please enter number for fibonachi: "))
for i in range(n):
    if i==0 or i==1:
        fib.append(1)
    else:
        fib.append(fib[i-1]+fib[i-2])
    
print(fib)
