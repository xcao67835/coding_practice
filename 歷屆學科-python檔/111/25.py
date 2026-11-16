# -*- coding: utf-8 -*-

a, b, c = 12, 7, 18
while b > 0:
    c = a % b
    a = b
    b = c

print(a + b + c)