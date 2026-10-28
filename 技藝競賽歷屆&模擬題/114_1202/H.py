# -*- coding: utf-8 -*-

m="BTCW"

a,b=map(lambda x:m.index(x),input().split())


if a-b in (-1,3):
    print(1)
elif a-b in (1,-3):
    print(2)
else:
    print(0)