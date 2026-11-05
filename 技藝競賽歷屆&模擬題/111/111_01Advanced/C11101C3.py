# -*- coding: utf-8 -*-

while 1:
    a,b=input().split()
    if a==b=="0":
        break
    
    
    a=list(map(int,list(a.zfill(10))))
    b=list(map(int,list(b.zfill(10))))
    c=[0]*10
    ans=0
    for i in range(9,-1,-1):
        c[i]+=a[i]+b[i]
        
        if c[i]>=10:
            c[i]-=10
            c[i-1]+=1
            ans+=1
            
    if ans==0:
        print("No carry operation.")
    elif ans==1:
        print("1 carry operation.")
    else:
        print(f"{ans} carry operations.")