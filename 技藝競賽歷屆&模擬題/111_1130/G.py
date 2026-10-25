# -*- coding: utf-8 -*-

for _ in range(int(input())):
    s = list(input())
    o=""
    dig=""
    while s:
        

        if 48<=ord(s[-1])<=57:
            dig+=s.pop()
        else:
            #print(dig)
            c = s.pop()
            dig=int(dig[::-1])
            o+=c*dig
            dig=""
            
    print(o[::-1])