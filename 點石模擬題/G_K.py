# -*- coding: utf-8 -*-

for _ in range(int(input())):
    #ans=orange*blue-(n-1)
    tree=dict()
    n=int(input())
    if n!=1:
        
    
        for i in range(1,1+n):
            i=str(i)
            tree[i]={"conn":[], "color":0}
            
        for i in range(n-1):
            a,b=input().split()
            
            tree[a]["conn"].append(b)
            tree[b]["conn"].append(a)
            
            
        stack=["1"]
        visi=set()
        col=0
        while stack:
            node=stack.pop()
            for i in tree[node]["conn"]:
                if i not in visi:
                    visi.add(i)
                    
                    if tree[node]["color"]==0:
                        tree[i]["color"]=1
                        col+=1
                    stack.append(i)
        
        ans=col*(n-col)-(n-1)
        print(ans)
    else:
        print(0)