# -*- coding: utf-8 -*-

tree=dict()
n=int(input())
for i in range(1,1+n):
    a,b=map(int,input().split())
    tree[i]={"child":(a,b)}
   
tree[1]["depth"]=0 
tree[1]["order"]=0   


stack=[(1,0,0)]
while stack:
    node,depth,order=stack.pop()
    for i in (0,1):
        if (tree[node]["child"][i] != 0):
            child=tree[node]["child"][i]
            tree[child]["depth"]=depth+1
            tree[child]["order"]=order*2+i
            stack.append((child,depth+1,order*2+i))

    
depths=[tree[i]["depth"] for i in range(1,1+n)]
mxd=max(depths)

sight=[]
layers=[[] for i in range(mxd+1)]
for i in range(1,1+n):
    layers[tree[i]["depth"]].append((i, tree[i]["order"]))
    
for i in range(mxd+1):
    layers[i].sort(key=lambda x:x[1])
    sight.append(layers[i][-1][0])
print(*sight)