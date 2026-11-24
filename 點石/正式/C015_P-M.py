n=int(input())
l=list(map(int,input().split()))
ans=0
now=0
height=0
for i in l:
    if height<i:
        ans+=now
        now=0
        height=i
    else:
        now+=height-i

now=0
height=0
for i in reversed(l):
    if height<=i:
        ans+=now
        now=0
        height=i
    else:
        now+=height-i

print(ans)