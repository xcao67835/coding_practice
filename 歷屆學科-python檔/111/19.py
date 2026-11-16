# -*- coding: utf-8 -*-

a = [92, 85, 80, 100, 78, 41, 34, 90, 60, 59]
count_1, count_2 = 0, 0
for i in range(10):
    if a[i] >= 80: count_1 += 1
    if a[i] < 60: count_2 += 1
print((count_1 + count_2) % 4)