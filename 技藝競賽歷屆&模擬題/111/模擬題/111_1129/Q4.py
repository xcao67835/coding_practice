# -*- coding: utf-8 -*-

while 1:
    try:
        s=input()
        a,c=s[0].lower(),s[-1].lower()
        t=len(s)%2
        if t:
            b=s[len(s)//2]
        else:
            b=s[len(s)//2-1].lower()+s[len(s)//2].lower()
        print(a,b,c,sep=",")
    except:
        break