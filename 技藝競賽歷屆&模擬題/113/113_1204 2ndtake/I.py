# -*- coding: utf-8 -*-

st=[0,0,0,0,0]
s=input()
sy='[!@#$^&*(),.?":{}|<>]'
if len(s)>=8:
    st[0]=1
for i in s:
    if i.isupper():
        st[2]=1
    if i.islower():
        st[3]=1
    if i.isdigit():
        st[1]=1
    if i in sy:
        st[4]=1
print(sum(st))
    