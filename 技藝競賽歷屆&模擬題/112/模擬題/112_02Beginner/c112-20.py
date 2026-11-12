# -*- coding: utf-8 -*-

n=int(input())
insu=set()

for i in range(1,int(n**.5+1)):
    if n%i==0:
        insu.add(i)
        insu.add(n//i)
        
if len(insu)>=5 and 3 not in insu and 5 not in insu:
    print(1)
else:
    print(0)