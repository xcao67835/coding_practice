# -*- coding: utf-8 -*-

while 1:
    try:
        y=int(input())

        #print(f"Case {i+1}: ",end="")
        
        if y%400==0:
            print("a leap year")
        elif y%100==0:
            print("a normal year")
        elif y%4==0:
            print("a leap year")
        else:
            print("a normal year")
    except EOFError:
        break