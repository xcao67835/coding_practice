# -*- coding: utf-8 -*-

a, s = 45, 0
while a > 0:
    s += a % 8
    a = a // 2
print(s % 4)