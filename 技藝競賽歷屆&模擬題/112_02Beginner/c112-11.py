# -*- coding: utf-8 -*-
from collections import Counter
word="Taipei"


s=input()
sc=Counter(s)
ans=0
loop=1
while loop:
    for i in word:
        if sc[i]>=1:
            sc[i]-=1
        else:
            loop=0
            break
    else:
        ans+=1
        
print(ans)