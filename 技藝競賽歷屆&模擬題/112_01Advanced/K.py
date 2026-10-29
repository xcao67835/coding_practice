# -*- coding: utf-8 -*-
re=[-1,-1,-1]
n=int(input())
if (n-1)//2500==0:
    re[0]=1
    
    re[1]=n//25 +(1 if n%25!=0 else 0)
    re[2]=n%25
    if re[2]==0:
        re[2]=25
    
elif (n-1)//2500 in (1,2):
    n-=2500
    re[0]=2
    
    
    re[1]=n//50+(1 if n%50!=0 else 0)
    re[2]=n%50
    if re[2]==0:
        re[2]=50
    
    
else:
    re[0]=3
    n-=7500
    
    
    re[1]=n//25 +(1 if n%25!=0 else 0)
    re[2]=n%25
    if re[2]==0:
        re[2]=25
print(*re)