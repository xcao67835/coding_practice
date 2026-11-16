# -*- coding: utf-8 -*-

def calc(x):
    if x < 2:
        return x
    return calc(x - 1) + calc(x - 2)

print(calc(5) % 4)