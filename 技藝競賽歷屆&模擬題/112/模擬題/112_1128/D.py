# -*- coding: utf-8 -*-
while 1:
    try:
        sx,sy,fx,fy,t=map(int,input().split(","))
        need=max(abs(sx-fx),abs(sy-fy))
        if need==0 and t==1:
            print("false")
            continue
        if t>=need:
            print("true")
        else:
            print("false")
        
    except EOFError:
        break