# -*- coding: utf-8 -*-

count = 0
data = [1, 2, 3]
data_length = len(data)
for i in range(data_length):
    for j in range(data_length):
        for k in range(data_length):
            if data[i] == data[j] or data[i] == data[k]:
               count += 1
print(count % 4)