# -*- coding: utf-8 -*-
l=input().replace(","," ").replace("."," ").split()
print(len(max(l,key=lambda x:len(x))))