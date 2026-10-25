# -*- coding: utf-8 -*-

while 1:
    a=  int(input())
    if a==0:
        break
    isl=0
    if a%400==0:
        isl=1
    elif a%100==0:
        isl=0
    elif a%4==0:
        isl=1
    
    if isl:
        print("a leap year")
    else:
        print("a normal year")