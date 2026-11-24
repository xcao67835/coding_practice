# -*- coding: utf-8 -*-
iii=0
while 1:
    try:
        iii+=1
        n=int(input())
        s=set()
        l=list(map(int,input().split()))
        no=0
        if l[0]<1 or l!=sorted(l):
            no=1
        for i in range(len(l)):
            if no:
                break
            for j in range(i+1):
                if l[i]+l[j] in s:
                    no=1
                    break
                s.add(l[i]+l[j])

            
        print(f"Case #{iii}: It is {'not 'if no else ''}a B2-Sequence.")
    except EOFError:
        break