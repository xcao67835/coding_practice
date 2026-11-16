# -*- coding: utf-8 -*-

a, b = 8, 4
c=0
while b > 0:
    c += a % b
    b -= 1
print(c % 4)