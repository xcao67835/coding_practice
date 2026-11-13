# -*- coding: utf-8 -*-

m=[["0","1"]]

n=int(input())
for i in range(n-1):
    m.append(["0"+i for i in m[-1]] + ["1"+i for i in m[-1][::-1]])
    
for i in m[-1]:
    print(i)