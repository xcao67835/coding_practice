# -*- coding: utf-8 -*-

a, s = 67, 0
while a > 0:
    s += a % 16
    a = a >> 1
print(s % 4)