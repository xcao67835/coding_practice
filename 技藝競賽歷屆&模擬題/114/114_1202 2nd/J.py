# -*- coding: utf-8 -*-

ips=list(map(int,input().split(".")))

ips=[bin(i)[2:].zfill(8) for i in ips]
print(*ips,sep="")