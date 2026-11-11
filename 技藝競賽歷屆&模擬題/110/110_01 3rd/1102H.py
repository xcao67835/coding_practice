# -*- coding: utf-8 -*-

for _ in range(int(input())):
    inp=input().split()
    v=[]
    for i in range(10):
        v.append(int(inp[i*2] + inp[i*2+1], 16))
        
    vv=hex(sum(v))[2:]
    
    while len(vv)>=5:
        vv = int(vv[:-4], 16)+int(vv[-4:],16)
        vv = hex(vv)[2:]
        
    vv=int(vv, 16)
    vv = ~vv&(16**4-1)
    print(hex(vv)[2:].zfill(4))
    
    
        
    