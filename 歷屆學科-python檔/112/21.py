# -*- coding: utf-8 -*-

str1 = "0 1 2 3 4 5 6 7 8 9 1"
b = list(map(int,str1.split()))
data = {}
for i in b:
    if i in data:
        data[i] += 1
    else:
        data[i] = 1

p = max(data.values())
print(p)