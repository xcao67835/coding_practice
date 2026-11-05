# -*- coding: utf-8 -*-
from collections import Counter
while 1:
    try:
        a=input()
        b=input()
        ca=Counter(a).items()
        cb=Counter(b)
        cc=[]
        
        for i in ca:
            aa=i
            bb=cb[aa[0]]
            
            cc.append((aa[0], min(aa[1],bb)))
            
        cc.sort(key=lambda x:x[0])
                
        for i in cc:
            print(i[0]*i[1],end="")
        print()
    except EOFError:
        break
    