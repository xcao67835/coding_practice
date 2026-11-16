# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    
    
    man=0
    ans=0
    for i in range(len(l)):
        status=l.pop()
        man+=1
        
        if man*status>=x:
            ans+=1
            man=0
            
    print(ans)