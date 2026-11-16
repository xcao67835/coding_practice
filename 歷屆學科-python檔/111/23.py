# -*- coding: utf-8 -*-

a = [[0] * 4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        if j % 2 == 0:
            a[i][j] = 2
        else:
            a[i][j] = 1


for i in range(1, 4):
    for j in range(1, 4):
        a[i][j] = a[i - 1][j] + a[i][j - 1]

print(a[3][3] % 4)