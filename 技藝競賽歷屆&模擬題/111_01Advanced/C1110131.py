# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
for _ in range(int(input())):
    y=int(input())
    
    if y%400==0:
        print("a leap year")
    elif y%100==0:
        print("a normal year")
    elif y%4==0:
        print("a leap year")
    else:
        print("a normal year")