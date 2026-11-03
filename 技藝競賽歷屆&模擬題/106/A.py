# -*- coding: utf-8 -*-

for _ in range(int(input())):
    s=input().split()
    ans=0
    for i in s:
        if "s" in i or "S" in i:
            ans+=1
    print(ans)