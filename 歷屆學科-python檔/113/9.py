# -*- coding: utf-8 -*-

result = 0
for i in range(1, 6):
    if i % 2 == 0:
        result += i
print(result % 4)