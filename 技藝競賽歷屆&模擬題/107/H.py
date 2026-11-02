# -*- coding: utf-8 -*-

for _ in range(int(input())):
    l2=list(map(int, input()[1:-1].split(",")))
    l=[i+1 for i in range(len(l2))]
    rl=[0]*len(l2)
    
    
   
    ans=[]
    for i in range(1,1+len(l)):
        if rl[i-1]!=0:
            continue
        ans.append([])
        visited=set()
        stack=[i]
        while stack:
            a=stack.pop()
            if a not in visited:
                visited.add(a)
                ans[-1].append(a)
                rl[a-1]=1
                
                stack.append(l2[a-1])
                
    print(str(ans))