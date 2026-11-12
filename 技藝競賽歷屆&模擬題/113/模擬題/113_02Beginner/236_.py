# -*- coding: utf-8 -*-
from collections import Counter
s=input()
l=[0]*(len(s)-1)
for i in range(len(s)-1):
    l[i]=ord(s[i+1])-ord(s[i])
    
l=list(map(lambda x:1 if x>0 else 0 if x==0 else -1, l))
cl=Counter(l)

if cl[0]==cl[-1]==0:
    print(1)
elif cl[0]==cl[1]==0:
    print(2)
else:
    print(3)