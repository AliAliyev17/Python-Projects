import random
a=input("1st DNA sequence:")
b=input("2nd DNA sequence:")
a1=[]
b1=[]
for i in a:
    a1.append(i)
for i in b:
    b1.append(i)
if len(a)>=len(b):
    c=len(b)
else:
    c=len(a)
dif=0
for i in range(c):
    if a1[i]==b1[i]:
        dif=dif
    else:
        dif+=1
dif+=abs(len(a)-len(b))
print(dif)
