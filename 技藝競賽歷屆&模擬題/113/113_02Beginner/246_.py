# -*- coding: utf-8 -*-
def f(x):
    x=list(x)
    l=[]
    for i in range(len(x)//2):
        l.append(int(x.pop()))
        l[-1]+=int(x.pop())*3
        
        l[-1]=str(l[-1])
    return "".join(l[::-1])
a,b=input().split(".")
a=("0" if len(a)%2==1 else "") + a 
b=b + ("0" if len(b)%2==1 else "")

print(f"{f(a)}.{f(b)}")