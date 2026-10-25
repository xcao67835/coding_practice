# -*- coding: utf-8 -*-

a = int(input())
ans=0
for i in range(1,a+1):
    b = bin(i)[2:]
    ans+=b.count("1")
print(ans)