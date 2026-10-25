# -*- coding: utf-8 -*-

while 1:
    tmp = input()
    if tmp=="0":
        break
    cost=0
    l = list(map(int,input().split()))
    while len(l)!=1:
        l.sort(reverse=1)
        a = l.pop()+l.pop()
        cost+=a
        l.append(a)
        
    print(cost)