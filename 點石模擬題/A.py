# -*- coding: utf-8 -*-
for _ in range(int(input())):
    a = int(input())
    
    can=False
    if a%2==0 and a!=2:
        can=True
    print("YES" if can else "NO")