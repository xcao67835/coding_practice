# -*- coding: utf-8 -*-
#input
V = 5
edges = [
    (4, 0, 1),  # A-B
    (2, 0, 2),  # A-C
    (1, 1, 2),  # B-C
    (5, 1, 3),  # B-D
    (8, 2, 3),  # C-D
    (10, 2, 4), # C-E
    (2, 3, 4),  # D-E
    (6, 1, 4)   # B-E
]

#def
chart=[-1]*V
#only edges
def find(x):
    if chart[x]!=-1:
        chart[x] = find(chart[x])
        return find(chart[x])
    return x
    
def merge(x,y):
    rx = find(x)
    ry = find(y)
    
    if rx!=ry:
        chart[rx]=ry
        return True
    
    return False

#main
edges.sort()
cost=0
count=0
MST=[]
for i in edges:
    w,x,y=i
    if merge(x,y):
        cost+=w
        MST.append(i)
            
        count+=1
        if count==V-1:
            break
        
connect=True
if count!=V-1:
    connect=False
        

print(cost)
print(MST)