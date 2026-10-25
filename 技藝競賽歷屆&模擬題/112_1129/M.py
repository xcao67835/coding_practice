# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n,x=map(int,input().split())
    l = list(map(int,input().split()))
    l.sort()
    ans=0
    group=[]
    while l:
        group.append(l.pop())
        if group[-1]*len(group)>=x:
            ans+=1
            group=[]
            
    print(ans)