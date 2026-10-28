# -*- coding: utf-8 -*-

ip = list(map(int,input().split(".")))

ip=list(map(lambda x:bin(x)[2:].zfill(8),ip))
print("".join(ip))