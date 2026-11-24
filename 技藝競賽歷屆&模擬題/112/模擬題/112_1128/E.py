# -*- coding: utf-8 -*-

from collections import deque
while 1:
    try:
        
        
        l,k=input()[1:].split("],")
        l=deque(map(int,l.split(",")))
        k=int(k)
        
        if k>len(l):
            print(max(l))
            continue
        
        win=0
        while 1:
            if l[0]>l[1]:
                win+=1
                if win==k:
                    print(l[0])
                    break
                
                l[0],l[1]=l[1],l[0]
                tmp=l.popleft()
                l.append(tmp)
            else:
                tmp=l.popleft()
                l.append(tmp)
        
        
    except EOFError:
        break