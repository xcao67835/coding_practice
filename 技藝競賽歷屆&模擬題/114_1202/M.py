# -*- coding: utf-8 -*-
fib=[1,2]

while fib[-1]<10**100:
    fib.append(fib[-1]+fib[-2])


for _ in range(int(input())):
    ans=0
    a,b=map(int,input().split())
    for i in fib:
        if a<=i<=b:
            ans+=1
        elif  i>b:
                break
            
    print(ans)