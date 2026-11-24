from bisect import bisect_left
n=int(input())
l=list(map(int,input().split()))
pm=float("-inf")
r=[]
ans=0
for i in l:
    idx=bisect_left(r,[i,1])
    if idx==len(r):
        r.append([i,1])
    else:
        if i==r[idx][0]:
            r[idx][1]+=1
        else:
            r.insert(idx,[i,1])
    ct=0
    for j in range(len(r)-1,idx,-1):
        ct+=r[j][1]
    ans+=ct
print(ans)