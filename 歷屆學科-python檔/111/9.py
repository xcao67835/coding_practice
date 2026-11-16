# -*- coding: utf-8 -*-

ans = 0
for i in range(1, 11):
    ans = ans + ans * i
print(ans % 4)    