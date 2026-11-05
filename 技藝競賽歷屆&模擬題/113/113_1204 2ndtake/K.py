# -*- coding: utf-8 -*-

import decimal
for _ in range(int(input())):
    a=decimal.Decimal(input()).quantize(decimal.Decimal("0.01") , rounding="ROUND_HALF_UP")
    if a==0:
        a=abs(a)
    print(a)