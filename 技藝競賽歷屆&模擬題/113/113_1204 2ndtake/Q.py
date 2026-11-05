V=int(input())
if V==1:
    print(0)
else:
    E=V-1
    from collections import defaultdict
    tree=defaultdict(list)
    for i in range(E):
        a,b=map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)
        
    stack=[(1,0)]
    visited={1}
    md=0
    fn=-1
    while stack:
        node,d=stack.pop()
        for nx in tree[node]:
            if nx not in visited:
                visited.add(nx)
                stack.append((nx, d+1))
                if d+1>md:
                    md=d+1
                    fn=nx
                
    dr=[None]+[0]*V
    stack=[(fn, 0)]
    visited={fn}
    while stack:
        node,d=stack.pop()
        dr[node]=max(dr[node], d)
        for nx in tree[node]:
            if nx not in visited:
                stack.append((nx, d+1))
                visited.add(nx)
                
    md=max(dr[1:])
    fn=dr.index(md)
    
    dr2=[None]+[0]*V
    stack=[(fn, 0)]
    visited={fn}
    while stack:
        node,d=stack.pop()
        dr2[node]=max(dr2[node], d)
        for nx in tree[node]:
            if nx not in visited:
                stack.append((nx, d+1))
                visited.add(nx)
                
    for i in range(1,1+V):
        print(max(dr[i], dr2[i]),end=" ")