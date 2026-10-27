# -*- coding: utf-8 -*-

while 1:
    ans=0
    a = int(input())
    if a==0:
        break
    if a==4:
        print(1)
        continue
    
    i,j=-1,-1
    
    for i in range(3,1+a//2):
        for j in range(2,int(i**.5+1)):
            if i%j==0:
                break
        else:
            ati=a-i
            for j in range(2,int(ati**.5+1)):
                if ati%j==0:
                    break
            else:
                ans+=1
            

            
    print(ans)