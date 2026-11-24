# -*- coding: utf-8 -*-

for _ in range(int(input())):
    s=input().split()
    ss=s.copy()
    
    count=0
    for i in range(len(ss)):
        if ss[i].isdigit() or ss[i]=="/":
            count+=1
        elif ss[i]=="X":
            count+=2
            
        if count==18:
            ind=i+1
            break
    

    if ind+2<=len(s)-1:
        last3=1
    else:
        last3=0
        
    for i in range(len(s)-1,-1,-1):
        if s[i].isdigit():
            s[i]=[int(s[i]), 1]
        elif s[i]=="/":
            if not (last3 and i == len(s)-2):
                if i+1<=len(s)-1:
                    s[i+1][1]+=1
            s[i]=[10-int(s[i-1]),1]
            
        elif s[i]=="X":
            if not (last3 and (i==len(s)-1 or i==len(s)-2 or  i==len(s)-3) ):
                if i+1<=len(s)-1:
                    s[i+1][1]+=1
                if i+2<=len(s)-1:
                    s[i+2][1]+=1
            s[i]=[10,1]
            
    sss = [i[0]*i[1] for i in s]
    print(sum(sss))
    
        
    