# -*- coding: utf-8 -*-

for _ in range(int(input())):
    cards=sorted(list(map(int,input().split())))
    #7
    for i in range(4):
        tmpc=[]
        for j in cards:
            
            if 1+i*13<=j<=13+i*13:
                tmpc.append(j-i*13)
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
    else:
        royal==False
        
    if royal:
        ans=7
        
            