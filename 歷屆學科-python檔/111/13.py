# -*- coding: utf-8 -*-

a = [[0] * 4 for _ in range(4)]
for i in range(1, 4):
    for j in range(1, 4):
        a[i][j] = a[i - 1][j - 1] + i + j

print(a[3][3])
