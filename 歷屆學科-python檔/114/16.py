# -*- coding: utf-8 -*-

x = 0
for i in range(5):
    if i % 2 == 0:
        continue
    if i == 4:
        break
    x += i
print(x % 4)