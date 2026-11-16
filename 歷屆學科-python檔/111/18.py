# -*- coding: utf-8 -*-

a, s = 33, 0
while a > 0:
    s += a % 16
    a = a >> 2
print(s % 4)