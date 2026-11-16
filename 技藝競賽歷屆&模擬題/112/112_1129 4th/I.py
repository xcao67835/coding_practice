# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n=int(input())
    *l,x=list(map(int,input().split()))
    
    s=set()
    st=0
    for i in l:
        if x-i in s:
            st=1
            break
        s.add(i)
        
    print("YES" if st else "NO")