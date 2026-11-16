# -*- coding: utf-8 -*-

i = s = 0
for j in range(4):
    while i < j:
        i = i + 2
    s = s + i
print(s % 4)