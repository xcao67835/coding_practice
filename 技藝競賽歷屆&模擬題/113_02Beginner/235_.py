# -*- coding: utf-8 -*-

l=list(input())
l=list(map(int,l))

if max(l)!=l[0] and max(l)!=l[-1] and l.count(max(l))==1:
    
    print(1)
else:
    print(0)