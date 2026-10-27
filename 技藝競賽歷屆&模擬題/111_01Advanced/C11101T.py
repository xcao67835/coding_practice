# -*- coding: utf-8 -*-

t = input().split(",")
pl=[]
def findprint(l,i):
    global pl
    srt=[]
    if i*2+1<=len(t)-1:
        if t[i*2+1] != "null":
            srt.append(findprint(l+[t[i]], i*2+1))
    if i*2+2<=len(t)-1:
        if t[i*2+2] != "null":
            srt.append(findprint(l+[t[i]], i*2+2))
            
    if srt:
        return srt
    else:
        pl.append(l+[t[i]])

findprint([], 0)
for i in pl:
    print("->".join(i))