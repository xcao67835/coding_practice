# -*- coding: utf-8 -*-

s=input()
ans=0
rep=0
noww=""

for i in s:
    if i==noww:
        rep+=1
        if rep>=3:
            ans+=1
    else:
        rep=1
        noww=i
print(ans)