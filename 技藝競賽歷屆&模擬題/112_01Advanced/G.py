# -*- coding: utf-8 -*-
chart=[0,1]
while 1:
    a=int(input())
    if a==0:
        break
    
    while len(chart)<a+1:
        chart.append((len(chart))**2+chart[-1])
        
    print(chart[a])