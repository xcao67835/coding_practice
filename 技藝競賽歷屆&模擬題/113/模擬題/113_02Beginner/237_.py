# -*- coding: utf-8 -*-

l=list(map(int,input().split(",")))
ans=0
for i in range(len(l)):
    can=True
    for j in range(len(l)):
        if l[j]%l[i]!=0:
            can=False
            break
    if can:
        ans+=1
        
print(ans)