# -*- coding: utf-8 -*-

arr = [0,1,2,3,4,5]
for i in arr:
    arr[i] = arr[i] + i

print(sum(arr) % 4)
