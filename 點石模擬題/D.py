# -*- coding: utf-8 -*-

from collections import defaultdict

for _ in range(int(input())):
    ppl=defaultdict(int)
    for _ in range(int(input())):
        
        s=input()
        if ppl[s]==0:
            print("OK")
        else:
            print(f"{s}{ppl[s]}")
        ppl[s]+=1
    
    