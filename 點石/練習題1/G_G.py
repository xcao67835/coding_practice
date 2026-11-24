# -*- coding: utf-8 -*-
from collections import Counter


for _ in range(int(input())):
    n=int(input())
    ppl=Counter(list(map(int,input().split())))
    ans=0
    while sum(ppl.values()):
        cap=0
        ans+=1
        
        while cap!=4:
            for i in range(4,0,-1):
                for j in range(ppl[i]):
                    if cap+i<=4:
                        cap+=i
                        ppl[i]-=1
                    else:
                        break
            else:
                break
                

                
    print(ans)
    
