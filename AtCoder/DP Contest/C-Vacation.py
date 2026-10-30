
n=int(input())
acti=[]
for i in range(n):
    acti.append(list(map(int,input().split())))
 
    
    
    
dp=[ [0]*3 for i in range(n)]
dp[0]=acti[0]

for i in range(1,n):
    for op in range(3):
        dp[i][op] = max(dp[i-1][op-1]+acti[i][op] , dp[i-1][op-2]+acti[i][op])
        
print(max(dp[-1]))