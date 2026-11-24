# -*- coding: utf-8 -*-

v=int(input())
items=[]
n=int(input())
for i in range(n):
    items.append(int(input()))

dp=[1]+[0]*v
for w in items:
    for i in range(v-w,-1,-1):
        dp[i+w] = dp[i+w]|dp[i]
      
i=1
while 1:
    if dp[-i]==1:
        break
    i+=1

print(i-1)
