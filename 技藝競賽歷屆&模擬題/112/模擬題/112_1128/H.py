# -*- coding: utf-8 -*-
while 1:
    try:
        ans=0
        l=list(map(int,input().split(",")))
        count=0
        last=0
        for i in l:
            if i>last:
                count+=1
                ans+=count
                last=i
            else:
                ans+=1
                count=1
                last=i
        print(ans)
        
        
    except EOFError:
        break