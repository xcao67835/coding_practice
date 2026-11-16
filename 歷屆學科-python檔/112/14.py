# -*- coding: utf-8 -*-

def g(n):
    if n >= 4:
        return n + g(n-1) + g(n-2)
    elif n >= 2:
        return g(n - 1) + g(n - 2)
    else:
        return 1

print(g(5) % 4)