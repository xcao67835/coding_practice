# -*- coding: utf-8 -*-

for _ in range(int(input())):
    inp=input().split()
    s=[]
    for i in range(10):
        s.append(int(inp[i*2]+inp[i*2+1], 16))
    
    s=sum(s)
    
    while len(hex(s)[2:]) >4:
        s = s%16**4 + s//16**4
        
    s=~s&(16**4-1)
    print(hex(s)[2:].zfill(4))        
    