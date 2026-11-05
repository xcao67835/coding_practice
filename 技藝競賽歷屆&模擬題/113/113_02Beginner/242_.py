# -*- coding: utf-8 -*-
from collections import defaultdict

s = input()
mxl = 0

for i in range(len(s) * 2 - 1):
    mid = i % 2
    i = i // 2

    ct = defaultdict(int)
    nl = mid - 1
    spr = 0

    while i - spr >= 0 and i + spr + mid < len(s):
        if s[i + spr + mid] != s[i - spr]:
            break

        nl += 2
        ct[s[i - spr]] += 1

        if len(ct) >= 3:
            mxl = max(mxl, nl)

        spr += 1

print(mxl)
"""
s = input()
mxl = 0

# 總共有 2*len(s) - 1 個可能的中心點
for i in range(len(s) * 2 - 1):
    left = i // 2
    right = left + (i % 2)
    
    # 向左右擴展
    while left >= 0 and right < len(s) and s[left] == s[right]:
        # 擷取當前的迴文子字串
        substring = s[left : right + 1]
        
        # 使用 set 檢查相異字元數量是否大於等於 3
        if len(set(substring)) >= 3:
            mxl = max(mxl, len(substring))
            
        left -= 1
        right += 1

print(mxl)"""