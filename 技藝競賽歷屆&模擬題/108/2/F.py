# -*- coding: utf-8 -*-

for _ in range(int(input())):
    a,b=map(int,input().split())
    print(f"{a//b}.",end="")
    a=a%b*10
    rec=[]
    visi=[a]
    idx=-1
    while a!=0:
        rec.append(a//b)
        a=(a%b)*10
        if a in visi:
            idx=visi.index(a)
            break
        visi.append(a)
    
    else:
        print(*rec,sep="",end="(0)\n")
    if idx!=-1:
        for i in range(len(rec)):
            if i==50:
                print("...",end="")
                break
            elif i==len(rec):
                break
            if i==idx:
                print("(",end="")
            print(rec[i],end="")
            
        print(")")