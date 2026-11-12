# -*- coding: utf-8 -*-

while 1:
    s=input()
    if s=="0":
        break
    
    a,b=s.split()
    a=int(a)
    l=[[] for i in range(a)]
    
    i=0
    while i<len(b):
        l[i//(len(b)//a)].append(b[i])
        i+=1
        
    
    for i in l:
        print(*i[::-1],sep="",end="")
        
    print()