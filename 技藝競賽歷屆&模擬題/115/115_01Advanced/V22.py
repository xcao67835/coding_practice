# -*- coding: utf-8 -*-

a = input().split(".")
a = list(map(lambda x:(bin(int(x))[2:]).zfill(8),a))
print("".join(a))