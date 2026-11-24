from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
a=int(input())
l=list(map(int,input().split()))
@lru_cache(None)
def find(n):
    if n==0:
        return 1
    if n==1:
        return 1
    ans=0
    for i in range(n):
        ans+=find(i)*find(n-i-1)
    return ans
for n in l:
    ans=find(n)
    print(ans%1000000007)