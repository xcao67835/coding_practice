# -*- coding: utf-8 -*-

from decimal import Decimal


for _ in range(int(input())):
    a=Decimal(input()).quantize(Decimal("0.01"), rounding="ROUND_HALF_UP")
    if a==0:
        a=abs(a)
    print(a)