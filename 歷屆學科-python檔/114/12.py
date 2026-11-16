# -*- coding: utf-8 -*-

nums = list(range(2, 12, 2))
s = 0
for i, v in enumerate(nums):
    if i % 2 == 0:
        s += v
print(s % 4)