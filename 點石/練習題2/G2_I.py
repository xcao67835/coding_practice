# -*- coding: utf-8 -*-

for _ in range(int(input())):
    _,*l=list(map(int,input().split()))
    left=min(l)
    right=max(l)
    if right==left:
        print(0)
        continue
    prev=float()
    while left!=right:
        mid=(left+right)//2
        a=b=0
        for i in l:
            a+=abs(i-mid)
            b+=abs(i-(mid+1))
        if a>b:
            left=mid+1
        else:
            right=mid
    print(min(a,b))