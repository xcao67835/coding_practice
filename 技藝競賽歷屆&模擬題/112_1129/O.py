# -*- coding: utf-8 -*-

n,m=map(int,input().split())
l = list(input().split())
for i in range(m):
    a ,b=l[n//2:], l[:n//2]
    l=[]
    for j in range(n//2):
        
        l.append(b[j])
        l.append(a[j])
print(*l)