# -*- coding: utf-8 -*-
from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    root,*l=list(map(int,input().split(",")))
    
    tree=defaultdict(lambda:[None,None])
    
    for node in l:
        stack=[root]
        while stack:
            parent=stack.pop()
            #print(parent)
            if node>parent:
                if tree[parent][1] is None:
                    tree[parent][1]=node
                else:
                    stack.append(tree[parent][1])
            if node<parent:
                if tree[parent][0] is None:
                    tree[parent][0]=node
                else:
                    stack.append(tree[parent][0])
        
    def f(root):
        if root is None:
            return []
        if root not in tree:
            return [root]
        
        
        return *f(tree[root][0]), *f(tree[root][1]), root
        
    print(*f(root),sep=",")