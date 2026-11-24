# -*- coding: utf-8 -*-

a,b=sorted(map(int,input().split()))
an=0
for i in range(a,b+1):
    if i%2==0:
        an+=i
        
print(an)