# -*- coding: utf-8 -*-

"""
TLE

while 1:
    try:
        s,d=map(int,input().split())
        l=[s]
        i=1
        while l[-1]<d:
            l.append(l[-1]+s+i)
            i+=1
        print(s+i-1)
            
                
    except EOFError:
        break
"""


