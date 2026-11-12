# -*- coding: utf-8 -*-

from decimal import Decimal
kk=int(input())
for i in range(kk):
    n=Decimal(input()).quantize(Decimal("0.01"), rounding="ROUND_HALF_UP")
    
    if n==0:
        print(abs(n))
    else:
        print(n)