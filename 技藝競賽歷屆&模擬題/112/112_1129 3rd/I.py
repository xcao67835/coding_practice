# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    t=l.pop()
    
    can=False
    
    s=set()
    for i in l:
        if t-i in s:
            can=True
            break
        else:
            s.add(i)
            
    print("YES" if can else "NO")