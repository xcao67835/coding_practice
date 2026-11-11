n=int(input())
l=list(map(int,input().split()))
mx=float("-inf")
now=0
for i in l:
    now=max(i,now+i)
    mx=max(mx,now)
print(mx)