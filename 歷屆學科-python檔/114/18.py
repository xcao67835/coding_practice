# -*- coding: utf-8 -*-

def g(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    return g(n - 1) + g(n - 3)

print(g(5) % 4)