n = int(input())
l=[1]
for i in range(n-1):
    l1=l+[0]
    l2=[0]+l
    l=[]
    for i in range(len(l1)):
        l.append(l1[i]+l2[i])

print(*l)