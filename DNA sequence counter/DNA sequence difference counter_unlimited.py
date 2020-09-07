n=int(input("Number of samples:"))
data=[]
for i in range(n):
    l=[]
    a=input("Genetic sequence:")
    a=a.upper()
    for i in a:
        l.append(i)
    data.append(l)

differences=[]
differ=[]
a=0
b=0
i=a+1
while a<(n-1):
    i=a+1
    while i<n:
        diff=0
        while b<len(data[a]) and b<len(data[i]):
            if data[a][b]!=data[i][b]:
                diff+=1
            diff+=abs(len(data[a])-len(data[i]))
            b+=1
        differ.append(diff)
        i+=1
        diff=0
        b=0
    differences.append(differ)
    differ=[]
    a+=1
print(differences)
