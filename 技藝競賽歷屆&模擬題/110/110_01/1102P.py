'''
# -*- coding: utf-8 -*-
from itertools import combinations

n=int(input())
l = list(map(int,input().split()))


a = set()

for i in range(1,n+1):
    for j in combinations(l, i):
        a.add(sum(j))
    
print(len(a))
print(*sorted(a))
'''

n=int(input())
s=set()
s.add(0)
coins=list(map(int,input().split()))
for i in coins:
    l=set([x +i for x in s])
    s=s.union(l)


s=sorted(s)
s=[i for i in s if i!=0]
print(len(s))
print(*s)