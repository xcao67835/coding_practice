# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n=int(input())
    ppl=sorted(list(map(int,input().split())),reverse=1)
    ans=0
    while len(ppl)>=2:
        for i in range(1,len(ppl)):
            if ppl[0]+ppl[i]<=4:
                ans+=1
                del ppl[i]
                del ppl[0]
                break
            elif ppl[0]==4:
                ans+=1
                del ppl[0]
                break
                
    else:
        ans+=len(ppl)
    print(ans)
    
