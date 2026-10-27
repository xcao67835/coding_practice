# -*- coding: utf-8 -*-

s=list(map(int,list(input())))

ss=sum(s)
ans=10-(ss%10)
if ans==10:
    ans=0
print(*s,ans,sep="")