# -*- coding: utf-8 -*-

n=int(input())
m=[]
for i in range(n):
    m.append(tuple(map(int,input().split())))
m.sort(key=lambda x:(x[1],x[0]))
ans=0
endtime=0
for a,b in m:
    if a>=endtime:
        ans+=1
        endtime=b
        
print(ans)