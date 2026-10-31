from collections import deque,defaultdict

n,m=8,8
edges=[
(1, 3),
(2, 3),
(2, 4),
(3, 5),
(4, 5),
(5, 6),
(5, 7),
(7, 8)]

indegree=[0]+[0]*n
graph=defaultdict(list)
for i in edges:
    a,b=map(int,i)
    graph[a].append(b)
    indegree[b]+=1
    
count=0
sems=0
rsems=[None]+[float("inf")]*n

def f(x):
    if indegree[x]==0:
        rsems[x] = sems+1
        q.append(x)
        indegree[x]=-1
        
q = deque()
for i in range(1,1+n):
    f(i)

while q:
    count+=len(q)
    sems+=1
    
    for _ in range(len(q)):
        i=q.popleft()
        nxtproj=graph[i]
        for nxt in nxtproj:
            indegree[nxt]-=1
            f(nxt)
    
if count!=n:
    print(-1)
else:
    print(sems)
    print(rsems)
            
            