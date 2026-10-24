# -*- coding: utf-8 -*-
default = [1970,1,1]
for _ in range(int(input())):
    date=default.copy()
    date[-1]+=int(input())
    odate=0
    while date!=odate:
        
        odate=date.copy()
        runyear=date[0]%400==0 or (date[0]%100!=0 and date[0]%4==0)
        if date[1] in (1,3,5,7,8,10,12) and date[2]>31:
            date[2]-=31
            date[1]+=1
        elif date[1]==2 and date[2]>28+runyear:
            date[2]-=28+runyear
            date[1]+=1
        elif date[1] in (4, 6, 9, 11) and date[2] > 30:
            date[2]-=30
            date[1]+=1
        if date[1]>12:
            date[1]-=12
            date[0]+=1
    date=map(lambda x:str(x).zfill(2),date)
    print("-".join(date))
            
            
