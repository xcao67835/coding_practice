# -*- coding: utf-8 -*-

a = int(input())
ans=set()
for i in range(1,int(a**0.5+1)):
    if a%i==0:
        ans.add(i)
        ans.add(a//i)
        
aa=0
ans=list(ans)
for i in ans:
    aa+=i
print(aa)