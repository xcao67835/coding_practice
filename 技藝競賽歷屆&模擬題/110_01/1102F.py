# -*- coding: utf-8 -*-
_=input()

l = list(map(int,input().split()))
forw=[]
ans=0
for i in l:
    for j in forw:
        if j>i:
            ans+=1
    forw.append(i)
            
print(ans)