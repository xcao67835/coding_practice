# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 21:08:45 2026

@author: user
"""
l={
"A":'10', 
"J":'18', 
"S":'26', 
"B":'11', 
"K":'19', 
"T":'27', 
"C":'12', 
"L":'20', 
"U":'28', 
"D":'13', 
"M":'21', 
"V":'29', 
"E":'14', 
"N":'22', 
"W":'32', 
"F":'15', 
"O":'35', 
"X":'30', 
"G":'16', 
"P":'23', 
"Y":'31', 
"H":'17', 
"Q":'24', 
"Z":'33', 
"I":'34', 
"R":'25'}

a = input()
re=0
t=int(l[a[0]])
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