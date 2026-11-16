# -*- coding: utf-8 -*-

a = [[1] * 4 for _ in range(4)]

for i in range(1, 4):
    for j in range(1, 4):
        if i == 1 and j == 1:
            a[i][j] = 2
        elif i == 1:
            a[i][j] = a[i][j - 1] + i
        elif j == 1:
            a[i][j] = a[i - 1][j] + j
        else:
            a[i][j] = a[i - 1][j] + a[i][j - 1]
print(a[2][2]% 4)
