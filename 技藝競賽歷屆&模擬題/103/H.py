# -*- coding: utf-8 -*-

for _ in range(int(input())):
    m,k,v=map(int,input().split(","))
    trees=[dict() for i in range(k)]
    for _ in range(m):
        node,*l=list(map(int,input().split()))
        
        if l[0]==999:
            root=node
            continue
        
        for i in range(k):
            trees[i][node]=l[i]
            
    r=[]
    for i in range(k):
        count=0
        stack=[v]
        while stack:
            n=stack.pop()
            if n!=root:
                count+=1
                stack.append(trees[i][n])
                
        r.append(count)
        
    print(*r,sep=",")
                    
        