# -*- coding: utf-8 -*-
from collections import Counter
while 1:
    try:
        l=list(map(float,input().split()))
        ll=[]
        for i in range(4):
            ll.append((l[i*2],l[i*2+1]))
        l=sorted(Counter(ll).items(), key=lambda x:x[-1],reverse=1)
        l = [i[0] for i in l]
        #l[0]為ans對角線上另一點
        
        
        ans=[0,0]
        for i in (0,1):
            ans[i] = l[1][i] + l[2][i] - l[0][i]
            
            
        for i in ans:
            print(f"{i:.3f}",end=" ")
        print()
        
        
    except EOFError:
        break