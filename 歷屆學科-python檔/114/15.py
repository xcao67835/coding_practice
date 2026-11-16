# -*- coding: utf-8 -*-

i = 1
total = 0
while i <= 3:
    for j in range(i):
        total += i + j
    i += 1
print(total % 4)