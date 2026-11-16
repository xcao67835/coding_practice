# -*- coding: utf-8 -*-

x = 0
n = 5
for i in range(n):
    for j in range(i - 1):
        for k in range(j - 1):
            x = x + 1

print(x % 4)