# -*- coding: utf-8 -*-

for _ in range(int(input())):
    _=input()
    l=list(map(int,input().split()))
    
    mx=float("-inf")
    now=float("-inf")
    for i in l:
        now=max(i,now+i)
        mx=max(mx,now)
        
        
    if mx>0:
        print(f"The maximum winning streak is {mx}.")
    else:
        print("Losing streak.")
    