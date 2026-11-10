# -*- coding: utf-8 -*-

from itertools import permutations
for _ in range(int(input())):
    n,a,b=input().split(",")
    
    p=sorted(permutations(n))
    a,b=int(a),int(b)
    a,b=int("".join(p[a-1])),int("".join(p[b-1]))
    print(a+b)