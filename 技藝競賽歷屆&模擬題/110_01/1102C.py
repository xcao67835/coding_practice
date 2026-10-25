# -*- coding: utf-8 -*-

while 1:
    try:
        l = list(input())
        ans=int(l.pop(0))
        for i in range(len(l)):
            ans+=int(l[i])*(1 if i%2==0 else -1)
        print(ans)
    except EOFError:
        break