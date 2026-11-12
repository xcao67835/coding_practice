# -*- coding: utf-8 -*-
while 1:
    try:    
        W=int(input())
        N=int(input())
        
        area=0
        for i in range(N):
            a,b=map(int,input().split())
            area+=a*b
            
        print(area//W)
    except EOFError:
        break