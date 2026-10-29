# -*- coding: utf-8 -*-
catch=[1]
while 1:
    try:
        n=int(input())
        while len(catch)<n:
            catch.append(catch[-1]+len(catch))
        print(catch[n-1])
    except EOFError:
        break