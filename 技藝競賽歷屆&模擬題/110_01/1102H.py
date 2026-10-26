# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

for _ in range(int(input())):
    inp=input().split()
    l=[]
    for i in range(10):
        l.append(inp[i*2]+inp[i*2+1])
    l = list(map(lambda x:int(x,16),l))
    ans=sum(l)


    ans=hex(ans)[2:]
    while len(ans)>4:
        a=ans[:-4]
        b=ans[-4:]
        ans=hex(int(a,16)+int(b,16))[2:]
    ans=int(ans,16)
    ans=hex(~ans&(16**4-1))[2:].zfill(4)
    print(ans)