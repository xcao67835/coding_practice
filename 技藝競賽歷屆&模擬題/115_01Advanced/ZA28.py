# -*- coding: utf-8 -*-
from collections import Counter
for _ in range(int(input())):
    cards=sorted(list(map(int,input().split())))
    ans=0
    #7
    royal=False
    for i in range(4):
        
        tmpc=[]
        for j in cards:
            
            if 1+i*13<=j<=13+i*13:
                tmpc.append(j-i*13)
        if tmpc:
            if tmpc[0]==1:
                
                tmpc.append(14)
        
        tmp=-1
        chain=1
        
        for k in tmpc:
            if k==tmp+1:
                tmp=k
                chain+=1

                if chain==5:
                    royal=True

                    break
            else:
                chain=1
                tmp=k
        if royal==True:
            break
    else:
        #4
        tmpc=cards.copy()
        tmpc=[i%13 if i%13!=0 else i%13+13 for i in tmpc]
        tmpc = list(set(tmpc))
        tmpc.sort()
        if tmpc[0]==1:
            tmpc.append(14)
        shun=False
        
        tmp=-1
        for k in tmpc:
            if k==tmp+1:
                tmp=k
                chain+=1

                if chain==5:
                    shun=True

                    break
            else:
                chain=1
                tmp=k
                
    tmpc=cards.copy()
    tmpc=[i%13 if i%13!=0 else i%13+13 for i in tmpc]
    count=list(Counter(tmpc).values())
    
    if royal:
        ans=7
    elif 4 in count or 5 in count:
        ans=6
    elif 3 in count and 2 in count:
        ans=5
    elif shun:
        ans=4
    elif 3 in count:
        ans=3
    elif count.count(2)>=2:
        ans=2
    elif 2 in count:
        ans=1
        
    print(ans)        