# -*- coding: utf-8 -*-

tt = input().split()
for _ in range(int(input())):
    n=input().split()
    a=b=0
    t=tt.copy()
    for i in range(4):
        if t[i]==n[i]:
            a+=1
            t[i]="d45fg6h7il"
            n[i]="efdsdgfrhgjygnbv"
            
    for i in range(4):
        if n[i] in t:
            b+=1
            t[t.index(n[i])] = 'edrfgthyjui'
            n[i]="gfhgytgrd"
            
    print(f"{a}A{b}B")