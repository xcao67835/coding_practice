# -*- coding: utf-8 -*-

m,s,n=map(int,input().split())
ppls=list(map(int,input().split()))
tar=s-(m-sum(ppls))
if tar<=0:
    print(0)
else:
    dp=[0]*(tar+1)
    
    
    for i in range(len(ppls)):
        for j in range(tar,0,-1):
            pre=dp[j-ppls[i]] if j-ppls[i]>=0 else 0
            if dp[j]<j:
                
                 dp[j]=pre+ppls[i]
            else:
                dp[j]=min(pre+ppls[i], dp[j])
    
    print(dp[-1])