# -*- coding: utf-8 -*-

r=[0]*1001
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    for i in range(a,b):
        r[i]+=1
    
mx=max(r)

mxl=0
nowl=0
posi=0
mxci=0

for i in range(1001):
    if r[i]==mx:
        if nowl==0:
            posi=i
        nowl+=1
        
        if nowl>mxl:
            mxci=posi
            mxl=nowl
            
    else:
        nowl=0
            
print(mx)
print(mxci,mxci+mxl)