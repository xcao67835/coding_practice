# -*- coding: utf-8 -*-

dp = [0 for _ in range(10)]
dp[0], dp[1], dp[2] = 0, 1, 2
for i in range(3, 8):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + i

print(dp[6] % 4)