# -*- coding: utf-8 -*-

n=input()

qi=0
for i in range(len(n)+1):
    nn=n[:i]+"5"+n[i:]
    for j in range(len(nn)+1):
        nnn=nn[:j]+"3"+nn[j:]
        nnn=int(nnn)
        #print(nnn)
        if nnn%21==0:
            qi=1
            break
    if qi:
        break
    
if qi:
    print(1)
else:
    print(0)