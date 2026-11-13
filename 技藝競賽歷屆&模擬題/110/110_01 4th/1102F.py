# -*- coding: utf-8 -*-

n=int(input())

l=list(map(int,input().split()))
def ms(l):
    if len(l)<=1:
        return l
    mid=len(l)//2
    left,right = ms(l[:mid]), ms(l[mid:])
    
    return merge(left, right)

ans=0

def merge(l,r):
    ct=0
    ll,rr = 0,0
    re=[]
    while ll<len(l) and rr<len(r):
        if l[ll]<=r[rr]:
            re.append(l[ll])
            ll+=1
            global ans
            ans+=ct
        else:
            re.append(r[rr])
            rr+=1
            ct+=1
            
    i=0
    while ll+i<len(l):
        ans+=ct
        i+=1
            
    re.extend(l[ll:])
    re.extend(r[rr:])
            
    return re

ms(l)

print(ans)