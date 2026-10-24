# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n = int(input())
    s = input()
    ans=set()
    for i in range(n-1):
        ss = s[:i]+s[i+2:]

        ans.add(ss)
    print(len(ans))