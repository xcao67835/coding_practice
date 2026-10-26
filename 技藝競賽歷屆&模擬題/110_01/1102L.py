# -*- coding: utf-8 -*-
while 1:
    try:
        n,c=map(int,input().split())
    except EOFError:
        break
    
    print(f"{n} {c}: ",end="")
    
    p = [1]
    for i in range(2,n+1):
        for j in range(2,int(i**0.5+1)):
            if i%j==0:
                break
        else: 
            p.append(i)
    k=len(p)
    
    if k%2!=0:
        k=k+1
        
    if c*2>=k:
        print(*p)
    else:
        print(*p[k//2-c:-(k//2-c)],end="\n\n")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
