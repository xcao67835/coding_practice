# -*- coding: utf-8 -*-

ans = 1
for i in range(2, 5):
    ans = ans * i + i
print(ans % 4)