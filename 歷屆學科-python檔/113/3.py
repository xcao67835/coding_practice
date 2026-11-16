# -*- coding: utf-8 -*-

count = 0
for i in range(3):
    for j in range(i, 5):
        count += 1
print(count % 4)