l = [0,0]+list(map(int,input().strip(" ").split(",")))
dp = [0]*len(l)
for i in range(2,len(l)):
    dp[i]=max(dp[i-1],dp[i-2]+l[i])
        
print(dp[-1])