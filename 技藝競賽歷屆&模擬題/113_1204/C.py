# -*- coding: utf-8 -*-
a=0
for _ in range(5):
    
    l=list(map(int,input().split()))
    l.sort()
    if l[2]<l[0]+l[1]:
        a+=1
print(a)