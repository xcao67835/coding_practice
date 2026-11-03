# -*- coding: utf-8 -*-

\
ch = "IVXLCDM"
ch2 = (1,5,10,50,100,500,1000)
def rom(s:str):
    if s=="":
        return 0
    
    c = ""
    for i in ch[::-1]:
        if i in s:
            c=i
            ind = s.index(c)
            indc = ch.index(c)
            break
        
    a, b = s[:ind], s[ind+1:]
    return(-rom(a)+ch2[indc]+rom(b))


for j in range(int(input())):
    print(rom(input()))