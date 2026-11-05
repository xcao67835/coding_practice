# -*- coding: utf-8 -*-
from collections import defaultdict

n,m=map(int,input().split())
cities = defaultdict(list)

for i in range(m):
    ta,tb=input().split()
    cities[ta].append(tb)
    
a,b=input().split()

stack=[a]
visited=set()

yes=False
while stack:
    nowcity = stack.pop()
    

    
    visited.add(nowcity)
    nextcities = cities[nowcity]
    for g in nextcities:
        if g == b or b == a:
            yes=True
            
            break
        
        if g not in visited:
            stack.append(g)
    if yes:
        print("Yes")
        break
    
else:
    print("No")
    
    