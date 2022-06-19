import math
second=int(input("Please enter second: "))
h=int(second/3600)
m= int((second % 3600)/60)
s=int(second % 60)
print("clock is: ",h,":",m,":",s)

