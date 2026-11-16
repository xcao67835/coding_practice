# -*- coding: utf-8 -*-

j, n = 0, 10
for i in range(1, n + 1):
    for k in range(i + 2, n - 1):
        j = j + 1

print(j % 4)