# -*- coding: utf-8 -*-

x = 0
n = 5
for i in range(n):
    for j in range(n):
        x = x + (j % 2)

print(x % 4)