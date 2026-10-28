# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n=int(input())
    fi=False
    for a in range(int(n**0.5+1)):
        for b in range(int(n**0.5+1)):
            for c in range(int(n**0.5+1)):
                if a**2 + b**2 +c**2==n:
                    print(a,b,c)
                    fi=True
                    break
            if fi:
                break
        if fi:
            break
    else:
        print(-1)