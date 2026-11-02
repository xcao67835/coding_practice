# -*- coding: utf-8 -*-

from collections import defaultdict

N,M=8,10
sides=[
(1, 2),
(2, 3),
(3, 1),
(3, 4),
(4, 5),
(5, 6),
(6, 4),
(6, 7),
(7, 8),
(8, 7)]

graph = defaultdict(lambda:{"in":[], "out":[]})
for i in sides:
    a,b=i
    graph[a]["out"].append(b)
    graph[b]["in"].append(a)