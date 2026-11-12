# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 21:43:33 2026

@author: user
"""


s = ['!','@','#','$','^','&','*','(',')',',','.','?','"',':','{','}','|','<','>']

st = 0
a=  input()
if len(a)>=8:
    st+=1
for i in a:
    if i.islower():
        st+=1
        break
for i in a:
    if i.isupper():
        st+=1
        break
for i in a:
    if i in s:
        st+=1
        break
for i in a:
    if i.isdecimal():
        st+=1
        break
    
print(st)