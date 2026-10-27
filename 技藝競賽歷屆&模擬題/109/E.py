# -*- coding: utf-8 -*-

for _ in range(int(input())):
    d = input()
   
    while 1:
        rd=d[::-1]
        
        if d==rd:
            print(rd)
            break
        
        d,rd=int(d),int(rd)
        d=d+rd
        d=str(d)