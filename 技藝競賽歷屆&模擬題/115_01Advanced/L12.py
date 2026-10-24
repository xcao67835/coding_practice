from decimal import Decimal,ROUND_HALF_UP

for _ in range(int(input())):
    a = Decimal(input())

    b = a.quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)
    if b==0:
        b="0.00"
    print(b)