# -*- coding: utf-8 -*-

for i in range(int(input())):
    a,b=map(int,input().split())
    ans=0
    for j in range(a,b+1):
        if j%2==1:
            ans+=j
            
    print(ans)