# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n=int(input())
    a=0
    for i in bin(n)[2:]:
        if i=="1":
            a+=1
            
    print(a)