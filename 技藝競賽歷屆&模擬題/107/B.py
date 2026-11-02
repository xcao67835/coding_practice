# -*- coding: utf-8 -*-
check=("012","345","678","036","147","258","048","246")
for _ in range(int(input())):
    l=[]
    for _ in range(3):
        l+=list(input())
    
    for i in check:
        a,b,c = map(int,list(i))
        if l[a]==l[b]==l[c] and l[a]!="0":
            print(l[a])
            break
    else:
        print(3)