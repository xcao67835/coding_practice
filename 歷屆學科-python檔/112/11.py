# -*- coding: utf-8 -*-

def f(a):
    if a == 0 or a == 1 or a == 2:
        return a
    return (f(a-1) + f(a-2) + f(a-3))

print(f(6) % 4)