# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:06:24 2026

@author: taiyu
"""

fib = [1,2]

while fib[-1]<10**100:
    fib.append(fib[-1]+fib[-2])
    
while 1:
    a,b = map(int,input().split())
    if a==b==0:
        break
    ans=0
    for i in fib:
        if i>b:
            break
        if a<=i:
            ans+=1
    print(ans)
            