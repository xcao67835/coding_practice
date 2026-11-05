# -*- coding: utf-8 -*-

a=int(input())
b=int(input())

ans=0
for i in range(a,b+1):
    ii=str(i)
    can=1
    for j in ii:
        if j=="0":
            can=0
            continue
        if i%int(j)!=0:
            can=0
    if can:
        ans+=1
        
print(ans)