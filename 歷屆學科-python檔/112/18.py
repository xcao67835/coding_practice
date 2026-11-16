# -*- coding: utf-8 -*-

total, i = 0, 0
while i <= 5:
    i = i + 1
    for j in range(1, i):
        if j % 2 == 1:
            total += 3
        else:
            total += 2

print(total % 4)
