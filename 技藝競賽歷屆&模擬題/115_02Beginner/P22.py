n = int(input())
di = dict()

for i in range(n):
    a,b,c=input().split()
    di[a]=(int(b)+int(c))/2

l = sorted(di,key=lambda x:(-di[x], x))

for i in range(n):
    print(f"{i+1} {l[i]} {di[l[i]]:.2f}")