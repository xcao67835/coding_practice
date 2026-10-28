# -*- coding: utf-8 -*-

s=list(input())
def tran(a):
    if a.isupper():
        return ord(a)+1000
    else:
        return ord(a)
    
s=list(map(tran,s))

mx=0
now=0
val=0
for i in s:
    if val<i:
        now+=1
        mx=max(mx,now)
        val=i
    else:
        now=1
        val=i
        
        
print(mx)