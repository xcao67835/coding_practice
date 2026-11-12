# -*- coding: utf-8 -*-

n=int(input())

l=[["0", "1"]]
for i in range(n-1):
    l.append(["0"+i for i in l[-1]]+["1"+i for i in l[-1][::-1]])
    
for i in l[-1]:
    print(i)