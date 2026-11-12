# -*- coding: utf-8 -*-
from collections import Counter
'''
(11,LL) (7,LLL) (8,R)
(5,) (4,L) (13,RL) (2,LLR) (1,RRR) (4,RR) ()
(3,L) (4,R) ()
(11,LL) (7,LLL) (2,LLL) (8,R)
(5,) (4,L) (13,RL) (2,LLR) (1,RRR) (4,RR) ()
'''

while 1:
    try:
        
        
        lnodes=[]
        while 1:
            bk=False
            orinodes=input()[1:-1].split(") (")
            
            for i in orinodes:
                
                if i=="":
                    bk=True
                    break
                i=i.split(",")
                lnodes.append(i)
            if bk:
                break
            
        layers=[]
        for i in lnodes:
            i.append(len(i[1]))
        lnodes.sort(key=lambda x:x[-1])
            
        for g in lnodes:
            if g[-1]+1>len(layers):
                for _ in range((g[-1]+1)-(len(layers))):
                    layers.append([])
                
            
            g[1]=g[1].replace("L","0").replace("R","1")
            if g[1]=="":
                g[1]=0
            else:
                g[1]=int(g[1],2)
                
            layers[g[-1]].append([g[0],g[1]])


        abnormal=False
        
        for layeri in range(len(layers)):
            layer = layers[layeri]
            player=[]
            
            if layeri!=0:
                lastlayer=[i[1] for i in layers[layeri-1]]
                for node in layer:
                    if node[1]//2 not in lastlayer:
                        abnormal=True
                        break
            if layer:
                replayer=max(Counter([i[1] for i in layer]).values())
                if replayer>=2:
                    abnormal=True
                    break
                    
        if abnormal:
            print("not complete")
        else:
            
            for layer in layers:
                layer=sorted(layer,key=lambda x:x[1])
                for i in layer:
                    print(i[0],end=" ")
            print()
                        #print(node)
                        
                
                
            
        
                
                
                
                
    except EOFError:
        break