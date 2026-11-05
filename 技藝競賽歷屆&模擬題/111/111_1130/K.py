# -*- coding: utf-8 -*-
while 1:
    a = int(input())
    if a==0:
        break
    b = a
    ans=set()
    while a!=1:
        for i in range(2,a+1):
            if a%i==0:
                a//=i
                ans.add(i)
                break
            
    print(f"{b} : {len(ans)}")