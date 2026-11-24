# -*- coding: utf-8 -*-

n,x=map(int,input().split())
l=list(map(int,input().split()))
l=list(enumerate(l))
l.sort(key=lambda x:x[1])
left=0
right=len(l)-1
ans=[]
while left!=right:
    s=l[right][1]+l[left][1]
    if s>x:
        right-=1
    elif s<x:
        left+=1
    else:
        ans.append(sorted((l[right][0],l[left][0])))
        right-=1
ans.sort()
if not ans:
    print("IMPOSSIBLE")
else:
    
    print(ans[0][0]+1, ans[0][1]+1)