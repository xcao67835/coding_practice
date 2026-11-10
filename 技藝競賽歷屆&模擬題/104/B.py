# -*- coding: utf-8 -*-

n=int(input())
t=input().split(",")

for i in range(n):
    ans=[0,0,0,0]
    
    ll=input().split(",")
    for k in range(6):
        l=ll.copy()
        del l[k]
        ct=0
        for j in l:
            if j in t:
                ct+=1
        if ct-2>=0:
            ans[ct-2]+=1
        
    print(*ans,sep=",")