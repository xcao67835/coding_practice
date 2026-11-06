# -*- coding: utf-8 -*-

l=[list(map(int,input().split())) for i in range(3)]
tg=0
for  i in l:
    tg+=sum(i)
tg//=2

for i in l:
    s=sum(i)
    i[i.index(0)]=tg-s
    print(*i)
