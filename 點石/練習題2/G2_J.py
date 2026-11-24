# -*- coding: utf-8 -*-

n=int(input())
l=list(map(int,input().split()))
mx=0
ans=0
for i in l:
    if i>mx:
        mx=i
    else:
        ans+=mx-i
print(ans)