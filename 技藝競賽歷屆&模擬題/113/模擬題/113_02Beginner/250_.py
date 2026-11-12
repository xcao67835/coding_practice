# -*- coding: utf-8 -*-
from collections import deque
s=deque("ABCDEF")
o=input()[1:-1].split("}{")
for i in o:
    i=  int(i)
    
    t=s.popleft()
    s.insert(i-1, t)

print(*s,sep="")