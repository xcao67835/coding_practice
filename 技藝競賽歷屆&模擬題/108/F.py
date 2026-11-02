# -*- coding: utf-8 -*-

for _ in range(int(input())):
    p=1
    bc,cs=map(int,input().split())
    a = bc//cs
    print(f"{a}.",end="")
    bc=bc%cs*10
    visited=[]
    res=[]
    while bc:
        if bc not in visited:
            visited.append(bc)
            
            res.append(bc//cs)
            bc=bc%cs*10
        else:
            ind=visited.index(bc)
           #res.append(bc//cs)
            break
            
    else:
        p=0
        print(*res, "(0)",sep="")
    
    if p:
        for i in range(len(res)):
            if i==ind:
                print("(",end="")
            print(res[i],end="")
            if i==49:
                print("...",end="")
                break
                
        print(")")