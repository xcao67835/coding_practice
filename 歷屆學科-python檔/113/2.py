# -*- coding: utf-8 -*-

a = [1, 2, 8, 4]
b = [2, 3, 4, 5]
total = 0
for i in range(4):
    total += a[i] * b[i]
print(total % 4)