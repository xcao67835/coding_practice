# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    
    mx=now=0
    
    for i in l:
        now = max(now+i,i)
        mx=max(mx,now)
        
    if mx>0:
        print(f"The maximum winning streak is {mx}.")
    else:
        print("Losing streak.")