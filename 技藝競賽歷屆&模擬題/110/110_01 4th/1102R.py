# -*- coding: utf-8 -*-
from collections import defaultdict
V,E=map(int,input().split())
gr=defaultdict(list)

for i in range(E):
    a,b=map(int,input().split())
    gr[a].append(b)
    
s,g=map(int,input().split())
stack=[s]
visi={s}
while stack:
    n=stack.pop()
    if n==g:
        print("Yes")
        break
    
    for nx in gr[n]:
        if nx not in visi:
            visi.add(nx)
            stack.append(nx)
    
else:
    print("No")