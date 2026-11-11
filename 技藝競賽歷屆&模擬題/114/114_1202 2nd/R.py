# -*- coding: utf-8 -*-

n,nn=map(int,input().split())
m=[]
for i in range(n):
    m.append(list(map(int,input().split())))
    
dist = [[0]*nn for i in range(n)]

for i in range(n):
    for j in range(nn):
        candidate = []
        if i-1>=0:
            candidate.append(dist[i-1][j])
        if j-1>=0:
            candidate.append(dist[i][j-1])
            
        if candidate:
            dist[i][j] = min(candidate)+m[i][j]
        
print(dist[-1][-1])