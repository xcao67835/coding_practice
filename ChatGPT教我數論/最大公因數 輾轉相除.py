# -*- coding: utf-8 -*-

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

def biggcd(n, l:list):
    if n>2:
        x, y = l.pop(), l.pop()
        l.append(gcd(x, y))
        return biggcd(n-1, l)
    else:
        return gcd(*l)
    
n = int(input())
l=list(map(int,input().split()))
print(biggcd(n, l))