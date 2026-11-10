# -*- coding: utf-8 -*-
from collections import Counter
for i in range(int(input())):
    c=list(map(int,input().split()))
    
    
    a4=0
    tc=set([i%13 if i%13!=0 else 13 for i in c])
    if 1 in tc:
        tc.add(14)
        
    for i in range(1,11):
        a=set(range(i,i+5))
        if tc&a==a:
            a4=1
            
    a7=0
    cat=[]
    for j in range(4):
        tc=set([i%13 if i%13!=0 else 13 for i in c if (i-1)//13==j])
        cat.append(tc)
        if 1 in tc:
            tc.add(14)
            
        for i in range(1,11):
            a=set(range(i,i+5))
            if tc&a==a:
                a7=1
                
                
    cc=sorted(Counter([i%13 for i in c]).values(), reverse=1)
    
    if a7:
        print(7)
    elif cc[0]>=4:
        print(6)
    elif cc[0]==3 and cc[1]>=2:
        print(5)
    elif a4:
        print(4)
    elif cc[0]==3:
        print(3)
    elif cc[0]==2 and cc[1]==2:
        print(2)
    elif cc[0]==2:
        print(1)
    else:
        print(0)