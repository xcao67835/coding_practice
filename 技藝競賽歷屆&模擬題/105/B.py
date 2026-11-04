# -*- coding: utf-8 -*-
dih={
'-----':0,
'.----':1,
'..---':2,
'...--':3,
'....-':4,
'.....':5,
'-....':6,
'--...':7,
'---..':8,
'----.':9}
for _ in range(int(input())):
    s=input().split()
    for i in s:
        print(dih[i],end="")
    print()