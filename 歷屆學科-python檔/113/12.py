# -*- coding: utf-8 -*-

n = 0
for i in range(10):
    if i % 3 == 0:
        n += i
print(n % 4)