l=list(map(int,input()))
a=set()
for i in range(len(l)):
    for j in range(i,len(l)+1):
        if sum(l[i:j])==10:
            a.add(str(l[i:j]))
print(len(a))