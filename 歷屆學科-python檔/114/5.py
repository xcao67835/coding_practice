# -*- coding: utf-8 -*-

cnt = 0
data = [1, 2, 3]
for i in data:
    for j in data:
        if i != j:
            cnt += 1
print(cnt % 4)
