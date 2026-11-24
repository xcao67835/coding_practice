ans=0
a,b=map(int,input().split())
if a>b:
    a,b=b,a
for i in range(a,b+1):
    if i%2==1:
        ans+=i**2

print(ans)