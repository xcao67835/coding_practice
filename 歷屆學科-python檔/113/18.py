# -*- coding: utf-8 -*-

x = 0
for i in range(3):
    for j in range(3):
        x += i * j
print(x % 4)