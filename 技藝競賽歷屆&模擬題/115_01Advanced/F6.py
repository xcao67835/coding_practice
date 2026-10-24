# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 20:28:48 2026

@author: user
"""
ch = ["A","B","C","D","E","F"]
for _ in range(int(input())):
    a,b = map(int,input().split())
    re = []
    if a==0:
        print(0)
        continue
    while a:
        tmp=a%b
        a = a//b
        if tmp>=10:
            tmp=ch[tmp-10]
        else:
            tmp=  str(tmp)
        re.append(tmp)
    re = re[::-1]
    print("".join(re))