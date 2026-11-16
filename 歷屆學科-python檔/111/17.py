# -*- coding: utf-8 -*-

total, i = 0, 0
while i <= 5:
    i = i + 1
    for j in range(1, i + 1):
        if j % 2 == 1:
            total += 1
        else:
            total += 2

print(total % 4)