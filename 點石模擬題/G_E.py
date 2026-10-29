# -*- coding: utf-8 -*-

n=int(input())
s=input()
rec=[""]*n
j=0
while j<len(s):
    for i in range(n*2-2):
        if i>=n:
            i=-(i-n)-2
        rec[i]+=s[j]
        j+=1
        if j==len(s):
            break

            
        
print(*rec,sep="")