# -*- coding: utf-8 -*-

n = int(input())
l = list(map(int,input().split()))

for i in l:
    while i!=1:
        if i%2==0:
            i//=2
        elif i%3==0:
            i//=3
        elif i%5==0:
            i//=5
        else:
            print("False")
            break
    else:
        print("True")
            
        