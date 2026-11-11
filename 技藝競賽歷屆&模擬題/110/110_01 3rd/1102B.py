# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n=int(input())
    if n%400==0:
        print("a leap year")
    elif n%100==0:
        print("a normal year")
    elif n%4==0:
        print("a leap year")
    else:
        print("a normal year")