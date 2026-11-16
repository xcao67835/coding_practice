# -*- coding: utf-8 -*-

nums = [1, 3, 5, 7]
A1 = all(n % 2 == 1 for n in nums)
A2 = any(n > 5 for n in nums)
print(f"{A1} {A2}")