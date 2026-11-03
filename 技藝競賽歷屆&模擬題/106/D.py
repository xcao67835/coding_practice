# -*- coding: utf-8 -*-
from itertools import permutations
for _ in range(int(input())):
    a,b,c = input().split(",")
    pa=(sorted(list(permutations(a))))
    
    b = pa[int(b)-1]
    c = pa[int(c)-1]
    
    aa=0
    for i in range(len(b)):
        if b[i]==c[i]:
            aa+=1
            
    print(f"{aa}A{len(b)-aa}B")