# -*- coding: utf-8 -*-

c = list("aeiouy")
a = list(input().lower())

for i in range(len(a)-1,-1,-1):
    if a[i] in c:
        del(a[i])

print("."+".".join(a))