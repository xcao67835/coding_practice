# -*- coding: utf-8 -*-
d={'C':12.01,'H':1.008,'O':16.00,'N':14.01}
for _ in range(int(input())):
    a=0
    count=""
    alp=""
    for i in input():
        if i.isalpha():
            if alp:
                a+=d[alp]*(int(count) if count else 1)
            alp=i
            count=""
        else:
            count+=i
            
    a+=d[alp]*(int(count) if count else 1)
    print(f"{a:.3f}")