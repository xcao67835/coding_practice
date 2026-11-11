from collections import Counter
d=dict()
n=int(input())
for i in range(n):
    a,b=input().split()
    b=int(b)
    d[a]=b

ld=list(d.items())
ld.sort(key=lambda x:(-x[1], x[0]))
for i in range(3):
    print(*ld[i])

cd=Counter(d.values())
m=list(cd.items())
m.sort(key=lambda x:(-x[1],-x[0]))
print(m[0][0])

v=d.values()
av=sum(v)/n
ov=0
for i in v:
    if i>av:
        ov+=1

print(ov)