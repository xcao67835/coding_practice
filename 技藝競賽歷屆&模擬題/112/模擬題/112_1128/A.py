# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 08:27:30 2026

@author: taiyu
"""
while 1:
    try:
        l=list(map(int,input().strip()[1:-1].split(",")))
        ll=[l[i]-l[i+1] for i in range(len(l)-1) if l[i]-l[i+1]!=0]
        if len(ll)==0:
            print("true")
            continue
        
        st=ll[0]
        
        can=1
        for i in ll:
            if st*i<0:
               can=0
               break
           
        print("true"  if can else "false")
        
        
    except EOFError:
        break
