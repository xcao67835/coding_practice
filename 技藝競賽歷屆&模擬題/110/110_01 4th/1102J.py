# -*- coding: utf-8 -*-

n=int(input())
l=list(map(int,input().split()))
for i in l:
    while i!=1:
        for j in (2,3,5):
            if i%j==0:
                i//=j
                break
            
        else:
            print(False)
            break
    else:
        print(True)