# -*- coding: utf-8 -*-

x = 0
for i in range(4):
    x += (i * i) % 3
print(x % 4)
