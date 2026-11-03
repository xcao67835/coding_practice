# -*- coding: utf-8 -*-

for _ in range(int(input())):
    a=list(map(int,list(input())))
    
    for i in range(len(a)):
        if i%2==0:
            a[i]*=2
            if a[i]>=10:
                a[i]-=9
                
    s = sum(a)
    
    if s%10==0:
        print("T")
    else:
        print("F")
        