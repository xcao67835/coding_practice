# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 21:19:06 2026

@author: user
"""


l={1: ['A', 'M', 'W'], 3: ['J', 'V', 'X'], 6: ['S', 'F'], 0: ['B', 'N', 'Z'], 2: ['K', 'L', 'Y'], 5: ['T', 'G'], 9: ['C', 'P', 'I'], 4: ['U', 'H'], 8: ['D', 'O', 'Q'], 7: ['E', 'R']}

a = input()
re=0
re+=int(a[0])*8
re+=int(a[1])*7
re+=int(a[2])*6
re+=int(a[3])*5
re+=int(a[4])*4
re+=int(a[5])*3
re+=int(a[6])*2
re+=int(a[7])*1
re+=int(a[8])*1

va=(10-(re%10))%10
a = l[va]
a.sort()
print("".join(a))
