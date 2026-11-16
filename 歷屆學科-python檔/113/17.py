# -*- coding: utf-8 -*-

a = [1, 2, 3, 4, 5]
b = [x * 2 for x in a if x % 2 == 0]
print(sum(b) % 4)