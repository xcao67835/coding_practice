# -*- coding: utf-8 -*-
from collections import defaultdict
d=defaultdict(lambda:"eh")
while 1:
    a = input()
    if a=="":
        break
    
    a,b = a.split()
    d[b]=a
    
while 1:
    try:
        c=input()
        print(d[c])
    except EOFError:
        break