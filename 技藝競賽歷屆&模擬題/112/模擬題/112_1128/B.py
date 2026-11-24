# -*- coding: utf-8 -*-

while 1:
    try:
        n=int(input())
        indegree=[None]+[0]*n
        out=[None]+[[] for i in range(n)]
        link=input()[2:-2].split("],[")
        times=[None]+list(map(int,input()[1:-1].split(",")))
        start=[None]+[0]*n
        mx=0
        stack=set(range(1,1+n))
        for i in link:
            a,b=map(int,i.split(","))
            indegree[b]+=1
            stack-={b}
            out[a].append(b)
            
        stack=list(stack)
        while stack:
            node=stack.pop()
            endtime=start[node]+times[node]
            mx=max(mx,endtime)
            
            for nx in out[node]:
                start[nx]=max(start[nx], endtime)
                indegree[nx]-=1
                if indegree[nx]==0:
                    stack.append(nx)
        print(mx)
    except EOFError:
        break