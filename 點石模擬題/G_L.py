# -*- coding: utf-8 -*-

n=int(input())

nodev=[0]+list(map(int,input().split()))
#nodev[node]=node value
tree=dict()
for i in range(1,1+n):
    tree[i]={"parent":-1, "child":[]}
for i in range(n-1):
    p,c=map(int,input().split())
    tree[c]["parent"]=p
    tree[p]["child"].append(c)
    
ti=tree.items()

for i in ti:
    if i[1]["parent"]==-1:
        root = i[0]
    
alt=True
day=0
while alt:
    alt=False
    leaf=[]
    stack=[root]
    tnodev=nodev.copy()
    delchild=[]
    while stack:
        node=stack.pop()
        childs=tree[node]["child"]
        
        for child in childs:
            if len(tree[child]["child"])==0 and nodev[child]<nodev[node]:
                if isinstance(tnodev[node], int):
                    tnodev[node] = [nodev[node], nodev[child]]
                elif isinstance(tnodev[node], list):
                    tnodev[node].append(nodev[child])
                tnodev[child]=0
                delchild.append(child)
            elif len(tree[child]["child"])!=0:
                stack.append(child)
                
    if tnodev!=nodev:
        day+=1
        alt=True
        for i in range(1,len(tnodev)):
            if i in delchild:
                tnodev[i]=0
            elif isinstance(tnodev[i], list):
                tnodev[i]=sum(tnodev[i])//len(tnodev[i])
                
        nodev=tnodev.copy()
    
        
        for g in delchild:
            for hh in range(len(tree.items())):
                h=list(tree.items())[hh]
                if g in h[1]["child"]:
                    del h[1]["child"][h[1]["child"].index(g)]
                    tree[h[0]]["child"] = h[1]["child"]
                    
            del tree[g]
            

print(day)
layers=[]
stack=[(root,0)]

while stack:
    node,depth=stack.pop()
    while len(layers)<depth+1:
        layers.append([])
    layers[depth].append(node)
    
    for i in tree[node]["child"]:
        stack.append((i, depth+1))
for i in range(len(layers)):
    layers[i].sort()
    for j in layers[i]:
        print(nodev[j],end=" ")
    print()
        
