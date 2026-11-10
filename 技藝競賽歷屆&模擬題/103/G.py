# -*- coding: utf-8 -*-

dig={"00":"0",
     "01":"1",
     "100":"2",
     "101":"3",
     "1100":"4",
     "1101":"5",
     "11100":"6",
     "11101":"7",
     "111100":"8",
     "111101":"9" }
cd={}
for i in range(26):
    cd[str((i+23)%26+1).zfill(2)]=chr(ord("A")+i)
    
    
    
    
for i in range(int(input())):
    s=input()
    ts=""
    means=""
    for i in s:
        ts+=i
        if ts in dig:
            means+=dig[ts]
            ts=""
            
    print(cd[means])
        