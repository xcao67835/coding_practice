# -*- coding: utf-8 -*-

total = 0
for i in range(1, 11):
    if i % 3 == 0:
        total += 1
print(total % 4)