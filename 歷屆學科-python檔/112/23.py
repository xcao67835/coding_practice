# -*- coding: utf-8 -*-

str1 = "0 1 2 3 4 5 6 7 8 9 1"
nums = list(set(map(int,str1.split())))
nums.sort()
print((nums[1]+ nums[2]) % 4)