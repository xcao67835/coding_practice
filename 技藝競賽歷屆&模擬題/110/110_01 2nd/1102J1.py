# -*- coding: utf-8 -*-

n=int(input())
l=list(map(int,input().split()))
for i in l:
    while 1:
        for j in (2,3,5):
            if i%j==0:
                i//=j
                break
        else:
            break
        
    if i==1:
        print(True)
    else:
        print(False)