n=int(input())
l=list(map(int,input().split()))
if n==1:
    print(l[0])
else:
    dp=[0]*n
    dp[0]=l[0]
    dp[1]=max(l[:2])
    for i in range(2,n):
        dp[i]=max(dp[i-1], dp[i-2]+l[i])

    print(dp[-1])