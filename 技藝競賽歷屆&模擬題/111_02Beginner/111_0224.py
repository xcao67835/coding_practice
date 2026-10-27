# -*- coding: utf-8 -*-

a=input()
b=input()
c=""

for i in range(max(len(a),len(b))):
    if i+1<=len(a):
        c+=a[i]
    if i+1<=len(b):
        c+=b[i]
        
print(c)