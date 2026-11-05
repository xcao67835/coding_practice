# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    target=l.pop()
    
    ans=False
    for i in l:
        ll = l.copy()
        del(ll[ll.index(i)])
        if target-i in ll:
            ans=True
            break
        
    if ans:
        print("YES")
    else:
        print("NO")