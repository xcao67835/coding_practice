# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 20:34:53 2026

@author: user
"""
ch=[
['Aquarius'   , 121  , 219],
['Pisces'     , 220  , 320],
['Aries'      , 321  , 420],
['Taurus'     , 421  , 521],
['Gemini'     , 522  , 621],
['Cancer'     , 622  , 722],
['Leo'        , 723  , 821],
['Virgo'      , 822  , 923],
['Libra'      , 924  , 1023],
['Scorpio'    , 1024 , 1122],
['Sagittarius', 1123 , 1222]
]

for _ in range(int(input())):
    d = input().split("/")
    if int(d[1])<10:
        d[1]="0"+d[1]
    d = "".join(d)
    d = int(d)
    for a,b,c in ch:
        if b<=d<=c:
            print(a)
            break
    else:
        print("Capricorn")


#Capricorn, 12/23 ∼ 1/20