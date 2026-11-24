# -*- coding: utf-8 -*-

from collections import defaultdict


while 1:
    try:
        c=defaultdict(int)
        l=list(map(int,input().split(",")))
        ans=0
        for i in l:
            ans+=c[i]
            c[i]+=1
            
        print(ans)
    except EOFError:
        break