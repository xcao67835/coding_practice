# -*- coding: utf-8 -*-
from collections import Counter
m,n=map(int,input().split())
arr=list(map(int,input().split()))
q=[]
for i in range(n):
    q.append((tuple(map(int,input().split())), i))
rec=[None]*n

block=int(m**.5)
q.sort(key=lambda x:(x[0][0]//block, x[0][1]))

right=left=0
c=Counter()
c[arr[0]]=1
count=1

for a,b in q:
    l,r=a
    while right!=r-1:
        if right<r-1:
            right+=1
            c[arr[right]]+=1
            if c[arr[right]]==1:
                count+=1
        elif right>r-1:
            c[arr[right]]-=1
            if c[arr[right]]==0:
                count-=1
            right-=1
            
    while left!=l-1:
        if left>l-1:
            left-=1
            c[arr[left]]+=1
            if c[arr[left]]==1:
                count+=1
        elif left<l-1:
            c[arr[left]]-=1
            if c[arr[left]]==0:
                count-=1
            left+=1
    
    rec[b]=count
    
for i in rec:
    print(i)