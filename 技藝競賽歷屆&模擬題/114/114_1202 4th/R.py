m,n=map(int,input().split())
mat=[]
for i in range(m):
    mat.append(list(map(int,input().split())))
    
dp=[[0]*n for i in range(m)]

for i in range(m):
    for j in range(n):
        if j==i==0:
            continue
        
        if i==0:
            dp[i][j]=dp[i][j-1]+mat[i][j]
        elif j==0:
            dp[i][j]=dp[i-1][j]+mat[i][j]
        else:
            dp[i][j]=min(dp[i-1][j],dp[i][j-1])+mat[i][j]
        
print(dp[-1][-1])