# -*- coding: utf-8 -*-
for _ in range(int(input())):
    amin,amax,bmin,bmax,mmin,mmax=map(int,input().split())
    ans=0
    for a in range(amin,amax+1):
        for b in range(bmin,bmax+1):
            for m in range(mmin,mmax+1):
                if (a-b)%m==(a+b)%m:
                    ans+=1
    print(ans)