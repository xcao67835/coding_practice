# -*- coding: utf-8 -*-

for _ in range(int(input())):
    a = int(input())
    if a%2==1:
        print(7,end="")
        a-=3
    print("1"*(a//2))
    