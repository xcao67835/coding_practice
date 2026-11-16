# -*- coding: utf-8 -*-

s = 0
val = 1
for _ in range(4):
    s += val
    val *= 2
print(s % 4)