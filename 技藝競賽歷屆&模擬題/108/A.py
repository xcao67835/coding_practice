# -*- coding: utf-8 -*-

n=int(input())
for i in range(n):
    s=input()
    count=0
    ans=0
    for i in s:
        if i=="O":
            count+=1
            ans+=count
        else:
            count=0
    print(ans)