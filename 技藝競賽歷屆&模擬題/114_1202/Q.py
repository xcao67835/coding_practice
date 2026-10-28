# -*- coding: utf-8 -*-

cp=[]
i=1
while i**2<=10**9:
    cp.append(i**2)
    i+=1
    
for _ in range(int(input())):
    a,b=map(int,input().split())
    ans=0
    for i in cp:
        if a<=i<=b:
            ans+=1
        elif i>b:
            break
        
    print(ans)