# -*- coding: utf-8 -*-

s=input()
m1,t1,m0,t0=0,0,0,0
for i in s:
    if i=="0":
        t0+=1
        m0=max(t0,m0)
        t1=0
    if i=="1":
        t1+=1
        m1=max(t1,m1)
        t0=0
        
print(abs(m1-m0))