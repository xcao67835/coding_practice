# -*- coding: utf-8 -*-

from itertools import permutations
s=input()
p=set(permutations(s))
ans=0
for i in p:

    if int("".join(i))%11==0:
        ans+=1
        
print(ans)