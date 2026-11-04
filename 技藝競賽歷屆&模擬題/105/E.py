# -*- coding: utf-8 -*-
for _ in range(int(input())):
    which="F"
    tree=list(map(int,input().split(",")))
    def leaf(node):
        r = []
        if node*2+1<len(tree):
            r.append(node*2+1)
        if node*2+2<len(tree):
            r.append(node*2+2)
            
        return r

    stack=[0]
    bi=1
    while stack:
        node=stack.pop()
        a=leaf(node)
        for i in range(len(a)):
            if i==0:
                if tree[a[i]]<tree[node]:
                    stack.append(a[i])
                else:
                    bi=0
                    break
            if i==1:
                if tree[a[i]]>tree[node]:
                    stack.append(a[i])
                else:
                    bi=0
                    break
                
                
                
    if bi :
        which="B"

    stack=[0]
    h1=1
    while stack:
        node=stack.pop()
        for i in leaf(node):
            if tree[i]>tree[node]:
                h1=0
                break
            else:
                stack.append(i)
                
    stack=[0]
    h2=1
    while stack:
        node=stack.pop()
        for i in leaf(node):
            if tree[i]<tree[node]:
                h2=0
                break
            else:
                stack.append(i)
                
    if h1 or h2:
        which="H"
        
    print(which)