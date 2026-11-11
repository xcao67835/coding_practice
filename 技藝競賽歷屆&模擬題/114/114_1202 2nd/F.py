# -*- coding: utf-8 -*-

t="hello"
i=0
s=input()
for j in s:
    if t[i]==j:
        i+=1
        if i==5:
            print("YES")
            break
else:
    print("NO")