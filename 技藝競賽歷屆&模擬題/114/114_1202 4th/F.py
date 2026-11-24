# -*- coding: utf-8 -*-

idx=0
for i in input():
    if i=="hello"[idx]:
        idx+=1
        if idx==5:
            print("YES")
            break
else:
    print("NO")