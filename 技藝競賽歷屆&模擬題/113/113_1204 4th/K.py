# -*- coding: utf-8 -*-

from decimal import Decimal
for i in range(int(input())):
    n=Decimal(input()).quantize(Decimal("0.01"),rounding="ROUND_HALF_UP")
    if n==0:
        print("0.00")
    else:
        print(n)