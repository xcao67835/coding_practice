# -*- coding: utf-8 -*-

for _ in range(int(input())):
    a=set(input().split()[1:])
    b=set(input().split()[1:])
    c=a&b
    
    print(len(c))