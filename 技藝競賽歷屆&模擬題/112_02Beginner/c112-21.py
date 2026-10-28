# -*- coding: utf-8 -*-

n=input()
if n.count("0")>1:
    print(0)
else:
    qi=0
    for i in range(len(n)):
        for j in range(len(n)-1):
            ncp=list(n)
            del ncp[i]
            del ncp[j]
                  
            nn=int("".join(ncp))
            if nn%21==0:
                qi=1
                break
        if qi:
            break
        
    if qi:
        print(1)
    else:
        print(0)