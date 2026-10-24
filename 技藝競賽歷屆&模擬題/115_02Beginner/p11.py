a = list(map(int,input().split()))
s = set()
for i in range(len(a)-1):
    s.add(a[i]-a[i+1])
print("YES" if len(s)<=1 else "NO")