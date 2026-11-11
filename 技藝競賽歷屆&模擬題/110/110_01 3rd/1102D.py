# -*- coding: utf-8 -*-

n=int(input())
l=list(map(int,input().split()))

a=sum(l)
odd = [i for i in l if i%2==1]
if a%2==1:
    a-=min(odd)
print(a)