# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n=int(input())
    if n==1:
        print("1 is not a prime number.")
        continue
    m=n
    for i in range(2,int(n**.5+1)):
        if n%i==0:
            print(f"{m} is not a prime number.")
            break
    else:
        if str(n)[:]==str(n)[::-1]:
            print(f"{m} is a prime number.")
            continue
            
            
        n=int("".join(str(n)[::-1]))
        
        for i in range(2,int(n**.5+1)):
            if n%i==0:
                print(f"{m} is a prime number.")
                break
        else:
            print(f"{m} is an emirp number.")
            
