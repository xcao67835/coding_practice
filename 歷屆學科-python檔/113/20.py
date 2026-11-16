# -*- coding: utf-8 -*-

a = [[0] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        a[i][j] = i + j
print(a[2][2] % 4)

