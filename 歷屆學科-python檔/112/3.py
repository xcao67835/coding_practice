# -*- coding: utf-8 -*-

a = 10
def fn_1():
    global a
    a = 1

def fn_2():
    a = 1
fn_1()
print(a, sep="", end=" ")
fn_2()
print(a)