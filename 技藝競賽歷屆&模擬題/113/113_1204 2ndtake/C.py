# -*- coding: utf-8 -*-
ans=0
for i in range(5):
    a,b,c = sorted(list(map(int,input().split())))
    if a+b>c:
        ans+=1
print(ans)