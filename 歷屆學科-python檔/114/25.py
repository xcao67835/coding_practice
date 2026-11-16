# -*- coding: utf-8 -*-

nums = [2, 4, 6, 8]
A1 = all(n % 2 == 0 for n in nums)
A2 = any(n > 10 for n in nums)
print(f"{A1} {A2}")