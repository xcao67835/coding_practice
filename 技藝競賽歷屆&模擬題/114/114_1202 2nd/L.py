# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n=int(input())
    mx=float("-inf")
    now=0
    l=list(map(int,input().split()))
    
    for i in l:
        now = max(now+i, i)
        mx=max(now,mx)
        
       
    
    if mx>0:
        print(f"The maximum winning streak is {mx}.")
    else:
        print("Losing streak.")