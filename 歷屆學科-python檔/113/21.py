# -*- coding: utf-8 -*-

def calc(x):
    if x == 0:
        return 4
    return calc(x - 1) + 4
print(calc(3) % 4)
