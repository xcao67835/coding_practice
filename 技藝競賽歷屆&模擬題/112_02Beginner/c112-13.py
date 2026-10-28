# -*- coding: utf-8 -*-
from itertools import permutations
l=list(map(int,input().split(",")))

if sum(l)%2==0:
    target=sum(l)//2
    pl=permutations(l,3)
    for i in pl:
        if sum(i)==target:
            print(1)
            break
    else:
        print(0)
    
else:
    print(0)