# -*- coding: utf-8 -*-

for _ in range(int(input())):
    itree=input().split(",")
    ptree=input().split(",")
    
    def potree(it,pt):
        if len(it)>=1:
            r=pt.pop(0)
            ind=it.index(r)
            
            return *potree(it[:ind],pt[:ind]),*potree(it[ind+1:],pt[ind:]),r
        
        else:
            return []
        
    print(",".join(potree(itree,ptree)))