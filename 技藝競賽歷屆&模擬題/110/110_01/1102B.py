# -*- coding: utf-8 -*-

for i in range(int(input())):
    a = int(input())
    if a%400==0:
        print("a leap year")
    elif a%100==0:
        print("a normal year")
    elif a%4==0:
        print("a leap year")
    else:
        print("a normal year")
        