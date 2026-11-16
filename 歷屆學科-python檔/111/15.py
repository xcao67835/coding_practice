# -*- coding: utf-8 -*-

total = 0
for i in range(3):
    for j in range(i, 4):
        total += 1

print(total % 4)