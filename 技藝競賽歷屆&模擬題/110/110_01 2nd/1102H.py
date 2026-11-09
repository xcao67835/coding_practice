# -*- coding: utf-8 -*-

for i in range(int(input())):
    l=input().split()
    n=[]
    for i in range(10):
        n.append(l[i*2]+l[i*2+1])
    n=[int(i,16) for i in n]
    sn=sum(n)
    sn=hex(sn)[2:]
    while len(sn)>4:
        a,b=sn[:-4],sn[-4:]
        sn=hex(int(a,16)+int(b,16))[2:]
        
    sn=~int(sn,16)&(16**4-1)
    sn=hex(sn)[2:]
    sn=sn.zfill(4)
    print(sn)