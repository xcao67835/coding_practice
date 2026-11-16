# -*- coding: utf-8 -*-

a, b = 0, 1
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)