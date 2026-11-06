# -*- coding: utf-8 -*-
while 1:
    sta=""
    n=int(input())
    if n==0:
        break
    if n%400==0:
        sta="leap"
    elif n%100==0:
        sta="normal"
    elif n%4==0:
        sta="leap"
    else:
        sta="normal"
        
    print(f"a {sta} year")