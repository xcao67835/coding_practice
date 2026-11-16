# -*- coding: utf-8 -*-

x = 0
for i in range(1, 10):
    if i % 3 == 0:
        continue
    x += 1
    if x == 4:
        break
print(x % 4)