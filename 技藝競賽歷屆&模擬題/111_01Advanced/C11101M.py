# -*- coding: utf-8 -*-

a = input()[2:-2]
a = a.split("],[")

l = [list(map(int,i.split(","))) for i in a]
nl=[]
#print(l)
for i in range(len(l)):
    nl.append([])
    for j in range(len(l)):
        nl[i].append(l[-(j+1)][i])
        
print("[",end="")
for ii in range(len(nl)):
    i=nl[ii]
    if ii!=0:
        print(",",end="")
    print("[",end="")
    print(*i,sep=",",end="")
    print("]",end="")
    
print("]")