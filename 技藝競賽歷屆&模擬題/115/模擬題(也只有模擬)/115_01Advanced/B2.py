# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 20:16:12 2026

@author: user
"""

a = int(input())+1911
if a%400==0:
    print(True)
elif a%100==0:
    print(False)
elif a%4==0:
    print(True)
else:
    print(False)
    