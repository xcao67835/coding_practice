# -*- coding: utf-8 -*-

s=input()
word="hello"
ind=0

for i in s:
    if i==word[ind]:
        ind+=1
        if ind==5:
            print("YES")
            break
        
else:
    print("NO")