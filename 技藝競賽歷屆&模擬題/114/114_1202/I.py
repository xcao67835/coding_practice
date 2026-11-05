# -*- coding: utf-8 -*-

"""
P 和O → 1 O 和K → 4 K 和E → 6
E 和M → 8 M 和O → 2 O 和N → 1
"""
s=list(map(lambda x:ord(x),input()))
for i in range(len(s)-1):
    print(abs(s[i]-s[i+1]),end="")
