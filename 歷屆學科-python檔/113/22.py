# -*- coding: utf-8 -*-

total = 0
for i in range(1, 5):
    total += i * (5 - i)
print(total % 4)