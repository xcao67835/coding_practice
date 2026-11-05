# -*- coding: utf-8 -*-

for _ in range(int(input())):
    jin=[]
    n=int(input())
    if n==1:
        print(0)
        continue
    while n!=1:
        for i in range(2,int(n**.5+1)):
            if n%i==0:
                jin.append(i)
                n//=i
                break
        else:
            jin.append(n)
            n//=n
            
    print(sum(jin))