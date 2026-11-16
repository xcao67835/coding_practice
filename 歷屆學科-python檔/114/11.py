# -*- coding: utf-8 -*-

a, b = 1, 10
steps = 0
while b > a:
    b -= 2
    a += 1
    steps += 1
print(steps % 4)