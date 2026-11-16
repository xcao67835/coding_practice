# -*- coding: utf-8 -*-

def calc(x):
    if x == 0:
        return 1
    return calc(x - 1) + 3

print(calc(4) % 4)