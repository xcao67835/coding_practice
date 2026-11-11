a,b=input().split()
n,m=map(int,input().split())
b=int(b)
if a=="R":
    b*=-1

l=[]
for i in range(n):
    l.append(input().split())

for i in range(n):
    for j in range(m):
        idx=(j+b)%m
        print(l[i][idx],end=" ")
    print()