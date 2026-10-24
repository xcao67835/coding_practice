# -*- coding: utf-8 -*-

a = int(input())
ans=[]
while a!=1:
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            ans.append(i)
            a//=i
            break
        
    else:
        ans.append(a)
        a=1
        
print(*ans)