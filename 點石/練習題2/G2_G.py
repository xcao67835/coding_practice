# -*- coding: utf-8 -*-

a,b,c,d,e,f=map(int,input().split())
if a*e==b*d:
    if c*e==b*f:
        print("Too many")
    else:
        print("No answer")
elif a==d==0 or b==e==0:
    print("Too many")
else:
    x=(c*e-b*f)/(a*e-b*d)
    y=(c*d-a*f)/(b*d-a*e)
    print(f"x={x:.2f}")
    print(f"y={y:.2f}")