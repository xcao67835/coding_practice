# -*- coding: utf-8 -*-

while 1:
    n=int(input())
    if n==0:
        break
    
    if n%400==0:
        print("a leap year")
    elif n%100==0:
        print("a normal year")
    elif n%4==0:
        print("a leap year")
    else:
        print("a normal year")