# -*- coding: utf-8 -*-

for _ in range(int(input())):
    a,b,n=map(int,input().split())
    ans=0
    for i in range(a,b+1):
        if str(n) in str(i):
            ans+=1
            
    print(ans)