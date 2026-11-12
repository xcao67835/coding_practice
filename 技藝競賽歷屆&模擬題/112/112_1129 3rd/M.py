# -*- coding: utf-8 -*-

for _ in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    
    ans=0
    ppl=0
    while l:
        sta=l.pop()
        ppl+=1
        
        if ppl*sta>=b:
            ans+=1
            ppl=0
            
    print(ans)