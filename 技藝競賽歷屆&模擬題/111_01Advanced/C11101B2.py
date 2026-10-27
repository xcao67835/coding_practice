# -*- coding: utf-8 -*-

from collections import Counter
for _ in range(int(input())):
    side=sorted(list(map(int,input().split())))
    cside=Counter(side)
    vcside=sorted(Counter(side).values(), reverse=1)
    
    if vcside[0]==4:
        print("square")
    elif vcside[0]==2 and vcside[1]==2:
        print("rectangle")
    elif sum(side[:-1])>=side[-1]:
        print("quadrangle")
    else:
        print("banana")