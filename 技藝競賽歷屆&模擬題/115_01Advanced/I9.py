# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 21:08:45 2026

@author: user
"""
l={
'10':A, 
'18':J, 
'26':S, 
'11':B, 
'19':K, 
'27':T, 
'12':C, 
'20':L, 
'28':U, 
'13':D, 
'21':M, 
'29':V, 
'14':E, 
'22':N, 
'32':W, 
'15':F, 
'35':O, 
'30':X, 
'16':G, 
'23':P, 
'31':Y, 
'17':H, 
'24':Q, 
'33':Z, 
'34':I, 
'25':R}

a = input()
re=0
t=l[a[0]]
re+=t%10*9
re+=t//10
re+=int(a[1])*8
re+=int(a[2])*7
re+=int(a[3])*6
re+=int(a[4])*5
re+=int(a[5])*4
re+=int(a[6])*3
re+=int(a[7])*2
re+=int(a[8])*1
re+=int(a[9])*1


if re%10==0:
    print("Y")
else:
    print("N")