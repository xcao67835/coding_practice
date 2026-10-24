# -*- coding: utf-8 -*-
l = []
while 1:
    try:
        t=input()
        if not t:
            break
        l.append(t)
        
    except EOFError:
        break
    
line,word,character= 0,0,0
line=len(l)
for i in l:
    temp=i.split()
    word+=len(temp)
    character+=len(i)+1

print(line,word,character)