# -*- coding: utf-8 -*-

n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
l.sort()
t=int(input())
for i in l:
    print(i)
print("Yes" if t in l else "No")
    