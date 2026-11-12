# -*- coding: utf-8 -*-
def ip(inp:str):
    a = inp.split(".")
    a = list(map(lambda x:(bin(int(x))[2:]).zfill(8),a))
    return a

for _ in range(int(input())):
    a = list(map(ip,input().split("/")))
    b = [""]*4
    c = [""]*4
    for i in range(4):
        for j in range(8):
            b[i]+="1" if int(a[0][i][j]) and int(a[1][i][j]) else "0"
            c[i]+="1" if int(a[0][i][j]) or not int(a[1][i][j]) else "0"
    
    b = map(lambda x:str(int(x,2)),b)
    c = map(lambda x:str(int(x,2)),c)
    print(".".join(b)+"/"+".".join(c))