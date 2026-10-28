# -*- coding: utf-8 -*-
from collections import Counter
a=list(input())
b=list(input())
c=[0 if a[i]==b[i] else 1 for i in range(len(a))]
sc=sum(c)
if sc==2:
    lena=len(a)
    for i in range(1,1+len(a)):
        i=lena-i
        if a[i]==b[i]:
            del a[i]
            del b[i]
            
    if len(a)==len(b)==2:
        if (a[0],a[1])==(b[1],b[0]):
            print(1)
        else:
            print(0)
    else:
        print(0)
            
elif sc==0:
    ma=max(Counter(a).values())
    if ma>=2:
        print(1)
    else:
        print(0)
        
else:
    print(0)