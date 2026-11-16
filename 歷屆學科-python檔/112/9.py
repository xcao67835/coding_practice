# -*- coding: utf-8 -*-

count = 0
p = 1
while p < 10:
    count = count + (p % 2)
    p = p + 1

print(count % 4)