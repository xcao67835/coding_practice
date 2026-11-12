# -*- coding: utf-8 -*-

for i in range(int(input())):
    i+=1
    n=input()
    a=n+"0"
    p=set()
    while a not in ("1", str(n), *p):
        p.add(a)
        a=list(a)
        a=list(map(int,a))
        a=sum([i**2 for i in a])
        a=str(a)
        
    
    if a=="1":
        print(f"Case #{i}: {n} is a Happy number.")
    else:
        print(f"Case #{i}: {n} is an Unhappy number.")
        
