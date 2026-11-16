# -*- coding: utf-8 -*-

str1 = "1 2 3 2 4 5 3 6"
nums = sorted(set(map(int, str1.split())))
print(len(nums) % 4)
