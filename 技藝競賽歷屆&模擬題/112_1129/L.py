# -*- coding: utf-8 -*-
n = []
for _ in range(int(input())):
    n.append(int(input()))
    n.sort()
    if len(n)%2==1:
        print(n[(len(n)-1)//2])
    else:
        print(int((n[len(n)//2]+n[len(n)//2-1])/2))
    #