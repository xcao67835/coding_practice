# -*- coding: utf-8 -*-

for _ in range(int(input())):
    a,b,c,d=map(int,input().split(","))
    m,am=[[],[]],[]
    
    for i in range(a):
        t=list(map(int,input().split()))
        if 9999 in t:
            idx=(0,i,t.index(9999))
        
        m[0].append(t)
        
    for i in range(c):
        t=list(map(int,input().split()))
        if 9999 in t:
            idx=(1,i,t.index(9999))
        
        m[1].append(t)
        
    for _ in range(a):
        am.append(list(map(int,input().split())))
        
        
    if idx[0]==0:
        pos=(idx[1], idx[2])
    else:
        pos=(idx[2], idx[1])
        
        
    val=0
    j=0
    while val==0:
        tot=0
        if idx[0]==0:
            p=(pos[0], j)
        else:
            p=(j, pos[0])
            
        for i in range(b):
            
            a1,b1=m[0][p[0]][i], m[1][i][p[1]]
                
            if i==pos[1]:
                val=a1*b1//9999
                continue
            
            tot+=a1*b1
        j+=1
        
    d1=am[p[0]][p[1]]-tot
    print(d1//val)