# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    tar=l.pop()
    no=1
    for i in range(n-1):
        for j in range(i):
            if l[i]+l[j]==tar:
                no=0
                break
        if not no:
            break
        
    if no:
        print("NO")
    else:
        print("YES")