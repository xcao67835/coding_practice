# -*- coding: utf-8 -*-

n=int(input())
l=list(map(int,input().split()))
#n=8
#l=list(map(int,"1 20 54 1 50 100 2000 50".split()))
ans=0
def ms(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    l = ms(arr[:mid])
    r = ms(arr[mid:])
    
    return merge(l,r)

def merge(l,r):
    global ans
    ct=0
    ll=rr=0
    res=[]
    while ll<len(l) and rr<len(r):
        if l[ll]<=r[rr]:
            res.append(l[ll])
            ll+=1
            ans+=ct
        else:
            res.append(r[rr])
            rr+=1
            ct+=1
    i=0
    while i+ll<len(l):
        ans+=ct
        i+=1
        
    res+=l[ll:]+r[rr:]
        
    return res

ms(l)
print(ans)