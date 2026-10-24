s=input()
d=dict()
for i in s:
    d[i]=d.get(i,0)+1
m=max(d.values())
print(list(d.values()).count(m))
