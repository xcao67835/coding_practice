from collections import defaultdict
n=int(input())
graph=defaultdict(list)
for i in range(n):
    thing,reci=input().split(":")
    for aa in reci.split(","):
        a,b=aa.split("*")
        b=int(b)
        graph[thing].append((a,b))

need=defaultdict(int)

tar=input()
def dfs(node,times):
    if node not in graph.keys() or len(graph[node])==0:
        need[node]+=times
    
    for a,b in graph[node]:
        dfs(a,b*times)

dfs(tar,1)


nl=list(need.items())
nl.sort(key=lambda x:(x[1], x[0]))
for i in nl:
    print(*i,sep="*")