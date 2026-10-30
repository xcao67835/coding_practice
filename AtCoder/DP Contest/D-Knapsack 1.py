n,w=map(int,input().split())

value=[]
for i in range(n):
    a,b=map(int,input().split())
    value.append((a,b))
    
dp=[0]*(w+1)

for i in value:
    for j in range(w,i[0]-1,-1):
        dp[j]=max(dp[j], dp[j-i[0]] + i[1])
        
print(dp[-1])