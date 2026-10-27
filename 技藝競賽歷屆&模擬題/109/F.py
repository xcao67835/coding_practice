# -*- coding: utf-8 -*-

for _ in range(int(input())):
    l=list(map(int,input().split()))
    best=float("-inf")
    current=float("-inf")
    for i in l:
        current = max(current+i, i)
        best=max(current,best)
        
    print(best)
    
"""
9
-1 -2
-10 -1 -1 2
216 -2
-2 1 -3 4 -1 2 -1 -5 5
-2 -3 4 -1 2 -1 -5 -3
-2 -3 -4 -1 -2 -1 -5 -3
2 3 4 5 7
-65535
-65535 1 65535
"""