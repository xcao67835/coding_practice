# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 20:23:18 2026

@author: user
"""

a,b=input().split()
if (a=="B" and b=="T") or (a=="T" and b=="C")or (a=="C" and b=="W")or (a=="W" and b=="B"):
    print(1)
elif (a=="T" and b=="B") or (a=="C" and b=="T")or (a=="W" and b=="C")or (a=="B" and b=="W"):
    print(2)
else:
    print(0)