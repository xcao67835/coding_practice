from collections import defaultdict
V,E=map(int,input().split())
graph=defaultdict(set)
for i in range(E):
    a,b=map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)

color=defaultdict(lambda:-1)
visi=set()
can=1
for i in range(1,1+V):
    if color[i]==-1:
        visi.add(i)
        color[i]=0
        stack=[i]
        while stack:
            node=stack.pop()
            for nx in graph[node]:
                if color[nx]==color[node]:
                    can=0
                    break

                if color[nx]==-1:
                    color[nx]=1-color[node]

                if nx not in visi:
                    visi.add(nx)
                    stack.append(nx)

            if not can:
                break

print("YES" if can else "NO")
                