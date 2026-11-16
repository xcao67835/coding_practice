# -*- coding: utf-8 -*-

def calculate(n):
    if n ==0:
        return 0
    return n + calculate(n - 1)

print(calculate(4) % 4)