s=list(input())
dp=[]
def f(s,c):

    if s[0]!=c and s[-1]!=c:

        return 1
    return 0

for i in range(len(s)):
    dp.append([0]*(len(s)-i))
    for j in range(len(s)-i):
        if i==0:
            dp[i][j]=1
        else:
            tmp1 = dp[i-1][j] + f(s[j:i+j],s[i+j])
            tmp2 = dp[i-1][j+1] + f(s[j+1:i+j+1],s[j])
            dp[i][j]=min(tmp1,tmp2)

print(dp[-1][0])